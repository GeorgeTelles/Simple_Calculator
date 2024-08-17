<div>
  <img src="https://raw.githubusercontent.com/GeorgeTelles/georgetelles/f69531ec6b293b5148563588a764c010015d315e/logo_clara.png" alt="logo clara" width="300" style="display: inline-block; vertical-align: top; margin-right: 10px;">
  <img src="https://raw.githubusercontent.com/GeorgeTelles/georgetelles/f69531ec6b293b5148563588a764c010015d315e/logo_dark.png" alt="logo dark" width="300" style="display: inline-block; vertical-align: top;">
</div>

# Simple Calculator

This project presents two distinct approaches for implementing a simple calculator in Python, highlighting code efficiency, security, and maintainability.

## Implementation with Conditional Statements (`if` and `elif`)

The first version of the calculator uses conditional structures to perform basic mathematical operations.

### Characteristics of this approach:

- **Manual Detailing**: Each mathematical operation (addition, subtraction, multiplication, division) is handled by separate blocks of code. This results in more code repetition and requires specific logic for each operation.
  
- **Maintenance and Extensibility**: Adding new operations requires inserting new `elif` blocks and managing specific error messages and results for each operation. As the number of operations grows, this approach can become impractical.
  
- **Error Handling**: Error handling is limited and needs to be explicitly implemented for each operation, especially to prevent issues like division by zero.

## Implementation with `eval`

The second version of the calculator uses the `eval` function to evaluate mathematical expressions provided by the user.

### Characteristics of this approach:

- **Compact Code**: Uses a single line of code to perform the mathematical operation, significantly reducing the amount of code needed and eliminating repetition associated with different mathematical operations.

- **Ease of Use**: Allows the user to input complete mathematical expressions directly, making the code more flexible and intuitive. This simplifies interaction with the calculator.

- **Security and Risk**: While `eval` provides an elegant solution, it can pose security risks as it executes any provided Python code. This can lead to vulnerabilities if user input is not trusted. The use of `eval` should be carefully considered and ideally avoided in production environments.

- **Error Handling**: The code uses a `try-except` block to handle errors more generally, capturing `SyntaxError`, `NameError`, and `ZeroDivisionError`. This enhances robustness by centrally managing invalid inputs.

## Conclusion

The `if` and `elif` approach offers more granular control and security but results in more extensive and less flexible code. The `eval` approach provides a more compact and flexible solution but presents security risks that need to be managed carefully. The choice between these methods will depend on the specific needs of the project and the execution environment.
