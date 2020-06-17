# Matrix.py
# Author: Jared Buehner
# Class: SDEV 300
# Professor: Muhammad Khan
# Date: 06/16/2020

# Imports.
from __future__ import print_function
import sys
import numpy as np

# Displays menu.
def menu():
    menu_items = {
        1: 'Addition',
        2: 'Subtraction',
        3: 'Matrix Multiplication',
        4: 'Element Multiplication',
        5: 'Start over (Clear matrices)',
        6: 'Quit (Exit application)'
    }

    try:
        userInput = input('Would you like to play? (y/n) ')

        if userInput.lower() == 'y':
            matrices = build_matrices()

            while matrices is not None: 
                print('\n~~~~~~~~~~~~~~~~~~~~\n')
                print('\nFirst Matrix:\n', * matrices[0], sep='\n')
                print('\nSecond Matrix:\n', * matrices[1], sep='\n')
                print('\n~~~~~~~~~~~~~~~~~~~~\n')

                # Display menu.
                for item in menu_items.keys():
                    print(item, menu_items[item])

                # Get user input.
                userSelection = int(input('\nMake a selection from the menu: '))

                # Adds matrices.
                if userSelection == 1:
                    add_matrices(matrices)
                # Subtracts matrices.
                elif userSelection == 2:
                    subtract_matrices(matrices)
                # Multiply matrices.
                elif userSelection == 3:
                    multiply_matrices(matrices)
                # Multiply matrix elements.
                elif userSelection == 4:
                    multiply_matrix_elements(matrices)
                # Clears and starts over.
                elif userSelection == 5:
                    start_over()
                # Exits the application.
                elif userSelection == 6:
                    quit_app()

                else:
                    print('\Enter a number 1-6.')
        else:
            print('\n******* Thanks for trying the matrix application! *******\n')

    except (KeyboardInterrupt, ValueError):
        print('\nError, please try again.\n')

    finally:
        sys.exit()

def build_matrices():
    errors = False
    matrices = [[], []]
    rows = 3
    columns = 3

    try:
        print('\nSeparate your elements with a space.',
              '\nUse enter to move to the next row.',
              '\nExample:\n1 2 3',
              '\n4 5 6',
              '\n7 8 9\n'
              '\nPlease enter your first %s x %s matrix: ' % (rows, columns))
        # Builds first matrix.
        for i in range(rows):
            matrices[0].append(list(map(float, input().rstrip().split())))

        print('\nPlease enter your second %s x %s matrix: ' % (rows, columns))
        # Builds second matrix.
        for i in range(rows):
            matrices[1].append(list(map(float, input().rstrip().split())))

    except (KeyboardInterrupt, ValueError):
        errors = True
        pass
    # Exits the application.
    finally:
        if errors:
            print('An error occurred, please try again.')
            sys.exit()

    np_matrix = np.array([matrices[0], matrices[1]])

    return np_matrix


def add_matrices(matrices):
    added_matrix = np.add(matrices[0], matrices[1])

    print('\nMatrices Added:\n',
          *added_matrix, sep='\n')

    transpose_matrix(added_matrix)
    find_mean(added_matrix)


def subtract_matrices(matrices):
    subtracted_matrix = np.subtract(matrices[0], matrices[1])

    print('\nMatrices Subtracted:\n',
        *subtracted_matrix, sep='\n')

    transpose_matrix(subtracted_matrix)
    find_mean(subtracted_matrix)


def multiply_matrices(matrices):
    multiplied_matrix = np.matmul(matrices[0], matrices[1])

    print('\nMatrices Multiplied:\n',
        *multiplied_matrix, sep='\n')

    transpose_matrix(multiplied_matrix)
    find_mean(multiplied_matrix)


def multiply_matrix_elements(matrices):
    multiplied_matrix = np.multiply(matrices[0], matrices[1])

    print('\nMatrices Multiplied by Elements:\n',
        *multiplied_matrix, sep='\n')

    transpose_matrix(multiplied_matrix)
    find_mean(multiplied_matrix)


def transpose_matrix(matrix):
    matrix_transpose = np.transpose(matrix)

    print('\nMatrix Transpose:\n',
          *matrix_transpose, sep='\n')

# Calculates mean of the columns and rows.
def find_mean(matrix):
    row_mean = matrix.mean(axis=1)
    column_mean = matrix.mean(axis=0)

    print('\nRow Mean Values:\t',
          row_mean,
          '\nColumn Mean Values:\t',
          column_mean)

# Returns menu.
def start_over():
    print('\nYour matrices have been cleared!\n')
    menu()

# Ends application.
def quit_app():
    print('\n****** Thanks for trying the Matrix Application! *******')
    sys.exit()


if __name__ == '__main__':
    print('\n******* Welcome to the Matrix Application! *******\n')
    menu()