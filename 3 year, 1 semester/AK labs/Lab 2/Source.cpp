#include <mpi.h>
#include <iostream>
#include <fstream>

using namespace std;

double * compute_partial_sum(int myrank, int ntasks, int n, double * matrix1, double * matrix2)
{
	double * partial_sum_matrix = new double[n*n];
	fill_n(partial_sum_matrix, n*n, 0);
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < n; ++j)
		{
			for (int k = myrank; k < n; k += ntasks)
			{
				partial_sum_matrix[i*n + j] += matrix1[i*n + k] * matrix2[k*n + j];
			}
		}
	}
	return partial_sum_matrix;
}

void print_matrix(double * matrix, int n) {
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < n; ++j) {
			cout << matrix[i*n + j] << " ";
		}
		cout << endl;
	}
}

void generate_input(int n) {
	ofstream outfile("input.txt");
	outfile << n << endl;
	int a;
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < n; ++j) {
			if (i != 0 || j != 0)
				outfile << " ";
			a = rand() % 1000;
			outfile << a;
		}
	}
	outfile << endl;
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < n; ++j) {
			if (i != 0 || j != 0)
				outfile << " ";
			a = rand() % 1000;
			outfile << a;
		}
	}
	outfile << flush;
}

#define RESULT_TAG 100
#define M_TAG 101
#define N_TAG 102
#define MATRIX_TAG 103
#define VECTOR_TAG 104

void main(int argc, char ** argv)
{
	//generate_input(3);
	int myrank, ranksize;
	MPI_Status status;

	int n;
	double * matrix1;
	double * matrix2;

	MPI_Init(&argc, &argv);       /* initialize MPI system */

	MPI_Comm_rank(MPI_COMM_WORLD, &myrank);    /* my place in MPI system */
	MPI_Comm_size(MPI_COMM_WORLD, &ranksize);  /* size of MPI system */

	if (myrank == 0)               /* I am the master */
	{
		char path[256];
		ifstream input_file;
		while (true)
		{
			cout << "Specify input file path: ";
			cin >> path;
			input_file = ifstream(path);
			if (input_file.is_open()) break;
			else cout << "Error opening file!\n";
		}
		input_file >> n;
		matrix1 = new double[n*n];
		matrix2 = new double[n*n];

		// Reading matrix
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < n; ++j) {
				input_file >> matrix1[i*n + j];
			}
		}
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < n; ++j) {
				input_file >> matrix2[i*n + j];
			}
		}
		print_matrix(matrix1, n);
		print_matrix(matrix2, n);
		system("pause");

	}

	MPI_Barrier(MPI_COMM_WORLD);  /* make sure all MPI tasks are running */

	if (myrank == 0)               /* I am the master */
	{
		/* distribute parameter */
		cout << "Master: Sending n, m, matrix and vector to MPI-Processes \n";
		for (int k = 1; k < ranksize; k++)
		{
			MPI_Send(&n, 1, MPI_LONG, k, N_TAG, MPI_COMM_WORLD);
			MPI_Send(matrix1, n*n, MPI_DOUBLE, k, MATRIX_TAG, MPI_COMM_WORLD);
			MPI_Send(matrix2, n*n, MPI_DOUBLE, k, MATRIX_TAG, MPI_COMM_WORLD);
		}
	}
	else {	/* I am a slave */
			/* receive parameters */
		MPI_Recv(&n, 1, MPI_LONG, 0, N_TAG, MPI_COMM_WORLD, &status);
		matrix1 = new double[n*n];
		matrix2 = new double[n*n];
		MPI_Recv(matrix1, n*n, MPI_DOUBLE, 0, MATRIX_TAG, MPI_COMM_WORLD, &status);
		MPI_Recv(matrix2, n*n, MPI_DOUBLE, 0, MATRIX_TAG, MPI_COMM_WORLD, &status);
	}

	/* compute my portion */
	double * result = compute_partial_sum(myrank, ranksize, n, matrix1, matrix2);
	MPI_Barrier(MPI_COMM_WORLD);

	if (myrank == 0)	/* I am the master */
						/* collect results, add up, and print results */
	{
		for (int k = 1; k < ranksize; k++)
		{
			double * partial_sum_matrix = new double[n*n];
			MPI_Recv(partial_sum_matrix, n, MPI_DOUBLE, k, RESULT_TAG, MPI_COMM_WORLD, &status);
			for (int i = 0; i < n; ++i)
			{
				for (int j = 0; j < n; ++j)
				{
					result[i*n + j] += partial_sum_matrix[i*n + j];
				}
			}
		}
		cout << "Master: Has collected sum from MPI-Processes \n";

		print_matrix(result, n);

		MPI_Barrier(MPI_COMM_WORLD);

		system("pause");
	}
	else {	/* I am a slave */
			/* send my result back to master */
		MPI_Send(result, n*n, MPI_DOUBLE, 0, RESULT_TAG, MPI_COMM_WORLD);
		MPI_Barrier(MPI_COMM_WORLD);
	}

	MPI_Finalize();
}