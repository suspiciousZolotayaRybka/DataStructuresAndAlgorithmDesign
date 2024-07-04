/**
 *
 * Name: Finehout, Isaac CMSC 315/6383 Date: Date: 1/17/2024
 *
 * This class encapsulates the input file and contains the following public methods:
 *
 * - A constructor that accepts the file name of the Java source file to be tested
 * and throws a FileNotFoundException if the file does not exist
 * - A method that returns the next character in the file excluding characters
 * that are inside either type of comment and characters in either character or string literals
 * - A toString() method that returns a string containing the current line number and character
 * number of the current character
 * - the handleNewLine() method that takes the output to the next line
 * - the handleComment() method that handles and skips over comments in the code
 * - the handleLiteral() method that handles and skips over literals in the code
 * - the handleHandlerNewLine() method that is used by handleNewLine() and handleLiteral() to create a new line without returning a value outside
 * - findLineIterator() method that uses a for loop to change char into its wrapper Character and stores it into a List to make a ListIterator
 * - verifyFile() verifies a file is valid and is used in the constructor
 * - declareFileVariables() declares the instances variables and is used in the constructor
 *
 */
package Asg1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.ListIterator;
import java.util.Scanner;
import java.util.Set;

public class JavaFile extends File {

	/**
	 *
	 */
	private static final long serialVersionUID = 1L;

	private final Set<String> DELIMITERS = new HashSet<>(Arrays.asList(new String[] { "[", "{", "(", ")", "}", "]" }));

	private Scanner fileScanner;

	private String line;
	private ListIterator<Character> lineIterator;
	private int indexCurrentCharInLine;

	private int charNum;
	private int lineNum;

	/**
	 * Constructor for JavaFile. Throws a file not found if the file doesn't exist.
	 * Throws an illegal argument exception if the file doesn't have the correct
	 * extension. Throws an illegal argument exception for empty files.
	 *
	 * @param fileName
	 * @throws FileNotFoundException, IllegalArgumentException
	 */
	public JavaFile(String fileName) throws FileNotFoundException, IllegalArgumentException {
		super(fileName);

		// Verify the file exists and has a valid extension
		verifyFile(fileName);

		// Declare all variables, and find the char for the first line
		declareFileVariables();
	}

	/**
	 * Return a string with info about the lineNum, charNum, current line length,
	 * current index in the line, and if there are lines remaining.
	 */
	@Override
	public String toString() {
		return String.format(
				"JavaFile: [lineNum=%d, charNum=%d, line.length()=%d, indexCurrentCharInLine=%d, fileScanner.hasNextLine()=%b]",
				lineNum, charNum, line.length(), indexCurrentCharInLine, fileScanner.hasNextLine());
	}

	/**
	 * Returns the next character in a JavaFile. Conditions determine three
	 * specialized methods to use. If no conditions are met, the next character is
	 * simply taken and returned.
	 *
	 * The specialized methods include: Returning to the next line if the end of the
	 * line is reached Handling comments when a forward slash is found Handling
	 * literals when an apostrophe or quotation marks are found
	 *
	 * @return
	 * @variable nextChar
	 */
	public Character nextChar() {

		Character nextChar;
		nextChar = lineIterator.next();
		indexCurrentCharInLine++;

		// If the next char is a delimiter, return the delimeter
		// Otherwise the flow forces lineNum and index to be lost via handleNewLine
		if (DELIMITERS.contains(String.valueOf(nextChar))) {
			charNum++;
			return nextChar;
		}

		// Perform a second new line check.
		if (indexCurrentCharInLine == (line.length() - 1)) {
			charNum++;
			return handleNewLine(nextChar);

			// Handle comments as they occur
		}
		if (nextChar == '/') {
			charNum++;
			return handleComment(nextChar);

			// Handle string literals as they occur
		} else if ((nextChar == '\'') || (nextChar == '\"')) {
			charNum++;
			return handleLiteral(nextChar);
		}
		// No file end, new lines, comments, or literals detected, return nextChar
		charNum++;
		return nextChar;
	}

	/**
	 * Check the file has not ended. Update all the variables for a new line.
	 *
	 * @param nextChar
	 * @return
	 */
	private Character handleNewLine(Character nextChar) {
		if (!(fileScanner.hasNextLine())) {
			// return null if there are no lines left
			return null;
		}
		// Otherwise handle the new line
		line = fileScanner.nextLine();
		indexCurrentCharInLine = -1;
		lineNum++;

		// If next line is blank, skip it
		while (line.isBlank()) {
			line = fileScanner.nextLine();
			lineNum++;
		}

		lineIterator = findLineIterator();

		return nextChar;
	}

	/**
	 * A method that can call the private method handleNewLine from outside the
	 * class
	 */
	public Character callHandleNewLine() {
		// Ensure pre-requesites are met to generate a new line
		if (indexCurrentCharInLine == (line.length() - 1)) {
			if (handleNewLine(' ') == null) {
				// If the return is null, break the loop to end the program
				return null;
			}
		}
		return ' ';
	}

	/**
	 * While the next char is /, continually scan for comments until an end sequence
	 * is detected. The method of scanning changes depending on if / or * follows
	 * the initial forward slash.
	 *
	 * @param nextChar
	 * @return
	 */
	private Character handleComment(Character nextChar) {
		// A loop is used to check for multiple single-line comments or multi-line
		// comments in a row.

		while (nextChar == '/') {

			// Find the second comment char.
			// Implementation changes depending on if it is / or *
			nextChar = lineIterator.next();
			indexCurrentCharInLine++;

			// Handle single line comments by simply going to the next line
			if (nextChar == '/') {
				if (handleHandlerNewLine() == null) {
					// return null if there is no new line
					return null;
				}
				// Find the new values if there is no new line
				nextChar = lineIterator.next();
				indexCurrentCharInLine++;
			}

			// Handle /* by continuing on until the last2 characters are */
			if (nextChar == '*') {
				char lastChar = ' ';
				StringBuffer last2 = new StringBuffer("/*");
				while (!last2.toString().equals("*/")) {

					// Handle a new line if it has been reached
					if (indexCurrentCharInLine == (line.length() - 1)) {
						if (handleHandlerNewLine() == null) {
							// return null if there is no new line
							return null;
						}
					}

					// Find the new values if there is no new line
					nextChar = lineIterator.next();
					indexCurrentCharInLine++;

					// Assign appropriate char values at 0 and 1 in last2
					lastChar = last2.charAt(1);
					last2.setCharAt(0, lastChar);
					last2.setCharAt(1, nextChar);
					// If the comment closer has been reached
					if (last2.toString().equals("*/")) {
						// Handle a new line if it has been reached
						if (indexCurrentCharInLine == (line.length() - 1)) {
							if (!(fileScanner.hasNextLine())) {
								// return null if there are no lines left
								// This is for if a comment is at the very end
								return null;
							}
							handleHandlerNewLine();
						}
						nextChar = lineIterator.next();
						indexCurrentCharInLine++;
					}
				}
			}

		}
		return nextChar;
	}

	/**
	 * Handles string and character literals for the nextChar() method. Skips over
	 * the literal until the closing key is found (" or '). Takes into account
	 * escape characters (\' and \")
	 *
	 * @param nextChar
	 * @return
	 */
	private Character handleLiteral(Character nextChar) {
		char lastChar;

		// Handle a new line if it has been reached
		if (indexCurrentCharInLine == (line.length() - 1)) {
			handleHandlerNewLine();
		}

		// Find the new values
		lastChar = nextChar;
		nextChar = lineIterator.next();
		indexCurrentCharInLine++;

		// Continue through the Scanner while the end quote is reached
		while (!((nextChar == '"') || (nextChar == '\''))) {
			// Handle a new line if it has been reached
			if (indexCurrentCharInLine == (line.length() - 1)) {
				handleHandlerNewLine();
			}

			// Find the new values
			lastChar = nextChar;
			nextChar = lineIterator.next();
			indexCurrentCharInLine++;

			// Ensure stringLiterals with escaped characters ("\"") are skipped
			if (((nextChar == '"') || (nextChar == '\'')) && (lastChar == '\\')) {
				// Find the new values
				lastChar = nextChar;
				nextChar = lineIterator.next();
				indexCurrentCharInLine++;
			}

			// Impossible to have two string literals in a row (as can happen with comments)
			// No need to check for this

		}

		// Find the final char value outside the
		// Handle a new line if it has been reached
		// (for strings that concatenate the next line)
		if (indexCurrentCharInLine == (line.length() - 1)) {
			handleHandlerNewLine();
		}

		// Find the new values
		nextChar = lineIterator.next();
		indexCurrentCharInLine++;

		// Handle a new line if it has been reached
		// For strings that end the line with a semicolon
		if (indexCurrentCharInLine == (line.length() - 1)) {
			handleHandlerNewLine();
		}

		return nextChar;
	}

	/**
	 * Handle a new line for the handler() methods
	 */
	private Character handleHandlerNewLine() {
		// Return null if there is no next line
		if (!fileScanner.hasNextLine()) {
			return null;
		}

		line = fileScanner.nextLine();
		lineNum++;
		// If next line is blank, skip it
		while (line.isBlank()) {
			line = fileScanner.nextLine();
			lineNum++;
		}
		indexCurrentCharInLine = -1;
		lineIterator = findLineIterator();

		return ' ';
	}

	/**
	 * Use a for loop to convert String array char into List<Character>
	 *
	 * @return
	 */
	private ListIterator<Character> findLineIterator() {

		// Create a line Iterator
		ArrayList<Character> lineList = new ArrayList<>();
		for (char c : line.toCharArray()) {
			lineList.add(c);
		}
		return lineList.listIterator();

	}

	/**
	 * Used in the constructor. Verifies the file exists and has a valid extension
	 * (.java or .jav)
	 *
	 * @param fileName
	 * @throws FileNotFoundException
	 * @throws IllegalArgumentException
	 */
	private void verifyFile(String fileName) throws FileNotFoundException, IllegalArgumentException {

		// Throw a FileNotFoundException if the file is not valid
		if (!new File(fileName).exists() || (fileName.length() < 6)) {
			throw new FileNotFoundException();
		}
		// Throw an IllegalArgumentException if the extension is invalid
		if (!(fileName.substring(fileName.length() - 4).equals(".jav")
				|| fileName.substring(fileName.length() - 5).equals(".java"))) {
			throw new IllegalArgumentException("Invalid File Extension");
		}
	}

	/**
	 * Used in the constructor. Declares all major file variables.
	 *
	 * @throws FileNotFoundException
	 * @throws IllegalArgumentException
	 */
	private void declareFileVariables() throws FileNotFoundException, IllegalArgumentException {

		// Declare the scanner
		fileScanner = new Scanner(this);

		// Read in a line until a non-blank line is encountered or the file ends
		line = " ";
		lineNum = 0;
		while (fileScanner.hasNextLine() && line.isBlank()) {
			line = fileScanner.nextLine();
			lineNum++;
		}

		// If the line is blank, that means the file is empty. Throw an Exception
		if (line.isBlank()) {
			throw new IllegalArgumentException("Blank file not accepted");
		}

		// Otherwise, the file is not blank and variables can be declared
		lineIterator = findLineIterator();
		indexCurrentCharInLine = -1;

		charNum = 0;
	}

}
