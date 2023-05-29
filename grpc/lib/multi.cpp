/**
 * @file
 * @brief This file contains the multi() and delete_arr() functions.
 */

#include <stdio.h>

/**
 * @brief Multiply two integers by 100 and return the result as an array.
 *
 * This function takes two integers, multiplies each of them by 100, and stores the results in an array.
 *
 * @param x The first integer.
 * @param y The second integer.
 * @return A dynamically allocated array of two integers containing the multiplied values.
 * @note The caller is responsible for freeing the memory allocated for the returned array using the delete_arr() function.
 */
extern "C" {
    int* multi(int x, int y) {
        int* c = new int[2];
        c[0] = x * 100;
        c[1] = y * 100;
        return c;
    }

    /**
     * @brief Delete a dynamically allocated array.
     *
     * This function frees the memory allocated for a dynamically allocated array.
     *
     * @param ptr Pointer to the dynamically allocated array to be deleted.
     */
    void delete_arr(int* ptr) {
        delete[] ptr;
    }
}
