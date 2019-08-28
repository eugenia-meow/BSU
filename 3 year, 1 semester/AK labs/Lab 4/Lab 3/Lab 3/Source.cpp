#include "mpi.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <iostream>
#include <fstream>

using namespace std;

#define N 50
double u[N + 2][N + 2];

double u_true(double x, double y) {
	return x * y*y*y + sin(x*y);
}

double f(double x, double y) {
	return 6*x*y-(x*x+y*y)*sin(x*y);
}

int main(int argv, char* argc[]) {
	int rank, size;
	double t1, t2;
	MPI_Status status;
	MPI_Init(&argv, &argc);

	MPI_Comm_size(MPI_COMM_WORLD, &size);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	t1 = MPI_Wtime();

	int M = ceil(1.0*N / size);
	double h = 1.0 / (N + 1);
	double eps = 1e-8;
	int start_row = M * rank + 1;
	int end_row;

	for (int i = 0; i < N + 2; i++)
	{
		for (int j = 0; j < N + 2; j++)
		{
			if (i == 0 || j == 0 || (i == N + 1) || (j == N + 1)) {
				u[i][j] = u_true(i*h, j*h);
			}
			else
				u[i][j] = 0;
		}
	}

	double dmax, d, dm;
	do 
	{ 
		dmax = 0;
		d = 0;
		if ((rank + 1) * M < N)
		{
			end_row = (rank + 1) * M;
		}
		else
		{
			end_row = N;
		}
		if (rank % 2 == 0) {
			if (rank > 0) {
				MPI_Send(u[start_row], N + 2, MPI_DOUBLE, rank - 1, start_row, MPI_COMM_WORLD);
				MPI_Recv(u[start_row - 1], N + 2, MPI_DOUBLE, rank - 1, start_row - 1, MPI_COMM_WORLD, NULL);
			}
			if (rank < size - 1) {
				MPI_Send(u[end_row], N + 2, MPI_DOUBLE, rank + 1, end_row, MPI_COMM_WORLD);
				MPI_Recv(u[end_row + 1], N + 2, MPI_DOUBLE, rank + 1, end_row + 1, MPI_COMM_WORLD, NULL);
			}
		}
		else {
			if (rank > 0) {
				MPI_Recv(u[start_row - 1], N + 2, MPI_DOUBLE, rank - 1, start_row - 1, MPI_COMM_WORLD, NULL);
				MPI_Send(u[start_row], N + 2, MPI_DOUBLE, rank - 1, start_row, MPI_COMM_WORLD);
			}
			if (rank < size - 1) {
				MPI_Recv(u[end_row + 1], N + 2, MPI_DOUBLE, rank + 1, end_row + 1, MPI_COMM_WORLD, NULL);
				MPI_Send(u[end_row], N + 2, MPI_DOUBLE, rank + 1, end_row, MPI_COMM_WORLD);
			}
		}
		dm = 0;
		
		for (int i=start_row; i <= end_row; ++i ) 
			for (int j = 1; j <= N; ++j)
			{
				double temp = u[i][j];
				u[i][j] = 0.25*(u[i - 1][j] + u[i + 1][j] + u[i][j - 1] + u[i][j + 1] - h*h*f(i*h, j*h));
				double dm = fabs(temp - u[i][j]);
				if (d < dm) 
					d = dm;
				
			}
		MPI_Allreduce(&d, &dmax, 1, MPI_DOUBLE, MPI_MAX, MPI_COMM_WORLD);
	} while ( dmax > eps );

	t2 = MPI_Wtime();
	if (rank == 0)
	{
		cout << "rank = " << rank << " time = " << t2 - t1 << endl;
	}

	if (rank == 0)
	{
		for (int i = 0; i < N + 2; i++)
		{
			for (int j = 0; j < N + 2; j++)
			{
				/*cout << u[i][j] << " " << u_true(i*h, j*h) << " " << h*i << " " << h*j << endl;*/
				//ofstream x_;
				//x_.open("x.txt");
				//for (int i = 0; i < N + 2; i++)
				//{
				//	x_ << i*h << " ";
				//}
				//x_.close();
				//ofstream u_;
				//u_.open("u.txt");
				//for (int i = 0; i < N + 2; i++)
				//{
				//	for (int j = 0; j < N + 2; j++)
				//	{
				//		u_ << u[i][j] << " ";
				//	}
				//	u_ << endl;
				//}
				//u_.close();
				//ofstream u_t;
				//u_t.open("u_t.txt");
				//for (int i = 0; i < N + 2; i++)
				//{
				//	for (int j = 0; j < N + 2; j++)
				//	{
				//		u_t << u_true(i*h, j*h) << " ";
				//	}
				//	u_t << endl;
				//}
				//u_t.close();
			}
		}
		system("pause");
	}
	MPI_Finalize();
}