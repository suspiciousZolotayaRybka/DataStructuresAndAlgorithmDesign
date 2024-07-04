package Asg1;

public class TestFile {
	public static void main(String[] args) {
		// This is a single-line comment (with a bracket that should be ignored)
		System.out.println("Hello, World!"); // Printing a string

		int[] numbers = { 1, 2, 3, 4, 5 }; // Array initialization

		/*
		 * This is a multi-line comment. It includes some delimiters: {}()[] These
		 * should also be ignored.
		 */

		// String literal with delimiters
//		String text = "(This is a [test] string {with} delimiters)";

		// Character literals
//		char leftBracket = '(';
//		char rightBracket = ')';

		if (numbers.length > 0) {
			System.out.println("Array is not empty.");
		}

		// Unmatched delimiters for testing
		// Uncomment the following line to test an unmatched delimiter
		// System.out.println("Unmatched [delimiter");
	}
}
