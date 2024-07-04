/**
 *
 * Name: Finehout, Isaac CMSC 315/6383 Date: 1/17/2024
 *
 * This class contains the main method.
 * It reads in the file name from the keyboard until a valid file name is
 * entered, and then creates an object of the first class. It then repeatedly
 * calls the first class's method to return the next character until it returns
 * null or a mismatch of delimeters is encountered.
 *
 * Matching delimiters include parentheses, braces, and square brackets.
 * Comments should not be included
 *
 */
package Asg1;

import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Stack;

public class Manager {

	private static Scanner stdin = new Scanner(System.in);

	/**
	 * The main method
	 *
	 * @param args
	 */
	public static void main(String[] args) {
		// javaFile is dynamic instead of static for clarity & method reusability
		JavaFile javaFile = readInFileName();
		verifyDelimiters(javaFile);
		stdin.close();
	}

	/**
	 * @formatter:off
	 * This method reads in userInput until a valid JavaFile is entered.
	 * It accomplishes this by nesting a try block inside a while loop.
	 * The while loop continues until the try block is able to complete without
	 * throwing an exception.
	 * Exceptions are thrown when an invalid filename, or a file extension other
	 * than .java or .jav is entered (these exceptions are thrown in
	 * the JavaFile constructor).
	 * After a valid JavaFile is entered, it returns the JavaFile outside the
	 * method.
	 * @formatter:on
	 *
	 * @variable file
	 * @variable isValidFile
	 * @variable userInput
	 * @variable JavaFile entered by the user
	 */
	private static JavaFile readInFileName() {
		JavaFile file = null;
		boolean isValidFile = false;
		String userInput = "";

		while (!isValidFile) {
			try {
				System.out.println("Please enter a valid Java (.java OR .jav) file: ");
				userInput = stdin.nextLine();
				file = new JavaFile(userInput);
				isValidFile = true;
			} catch (FileNotFoundException e) {
				System.out.println("Invalid file path: " + userInput);
			} catch (IllegalArgumentException e) {
				System.out.println("Invalid file path: " + userInput);
			}
		}

		return file;
	}

	/**
	 * Scan the file while nextChar() does not return null. If a delimiter is open,
	 * push it onto javaStack. If a delimiter is closed, pop it from javaStack and
	 * verify the last and next delimiters are the same.
	 *
	 * @variable nextDelimiter
	 * @variable javaStack
	 * @param javaFile
	 */
	private static void verifyDelimiters(JavaFile javaFile) {

		boolean hasValidDelimiters = true;
		Character nextDelimiter = javaFile.nextChar();
		Stack<Character> javaStack = new Stack<>();

		while (nextDelimiter != null) {

			// If the nextChar is an open delimiter, push it to the stack
			if ((nextDelimiter == '[') || (nextDelimiter == '{') || (nextDelimiter == '(')) {
				javaStack.push(nextDelimiter);
				// Handle the new line after using the delimiter
				javaFile.callHandleNewLine();

				// If the nextChar is a close delimiter pop it from the stack
			} else if ((nextDelimiter == ']') || (nextDelimiter == '}') || (nextDelimiter == ')')) {

				if (javaStack.isEmpty()) {
					// No valid delimiters if no delimiters exist for a closing delimiter
					hasValidDelimiters = false;
					break;
				}
				Character lastDelimiter = javaStack.pop();

				// printDelimiterError if the delimiters do not match
				if (((lastDelimiter == '[') && (nextDelimiter != ']'))
						|| ((lastDelimiter == '{') && (nextDelimiter != '}'))
						|| ((lastDelimiter == '(') && (nextDelimiter != ')'))) {
					printDelimiterError(lastDelimiter, nextDelimiter, javaFile);
					hasValidDelimiters = false;
					// Break out of the loop in case of invalid delimiters
					break;
				}
				// Handle the new line after using the delimiter
				if (javaFile.callHandleNewLine() == null) {
					// If null is returned, break out of the loop to exit
					break;
				}
			}
			nextDelimiter = javaFile.nextChar();

		}

		// If the stack is not empty, extra delimiters are present
		if (!javaStack.isEmpty() || !hasValidDelimiters) {
			System.out.println("Delimiter mismatch: Extra Delimiters detected");
			hasValidDelimiters = false;
		}

		// If everything executed correctly, print
		if (hasValidDelimiters) {
			System.out.println("The file entered has valid delimiters.");
		}
	}

	/**
	 * A method that prints the delimiter error information
	 *
	 * @param lastDelimiter
	 * @param nextDelimiter
	 */
	private static void printDelimiterError(Character lastDelimiter, Character nextDelimiter, JavaFile javaFile) {
		System.out.printf("Delimeter mismatch detected: [lastDelimiter=%c, nextDelimiter=%c]%n", lastDelimiter,
				nextDelimiter);
		System.out.println("javaFile information at mismatch: " + javaFile);
	}

}