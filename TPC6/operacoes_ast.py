class Operation:
    def __init__(self, op, num,next_op):
        self.op = op 
        self.num = (int)(num) 
        self.next_op = next_op 

    # Operation(2, '+', Operation(3, '*', Operation(4, None, None)))

    def pp(self):
        print(f"({self.op} {self.num}", end="")
        if isinstance(self.next_op, EmptyOperation):
            print("())", end="")
        elif self.next_op:
            self.next_op.pp()
            print(")", end="")

    def copy(self):
        """Creates a deep copy of the operation list to preserve the original."""
        if self.next_op is None or isinstance(self.next_op, EmptyOperation):
            return Operation(self.op, self.num, None)  # Copy without next op

        return Operation(self.op, self.num, self.next_op.copy())


    def calculate_priority_op(self):

        copy_op = self.copy()

        current = copy_op
        while current and current.next_op:
            if current.next_op.op in ('*', '/'):

                next_op = current.next_op

                if next_op.op == '*':
                    current.num *= next_op.num
                elif next_op.op == '/':
                    current.num /= next_op.num

                current.next_op = next_op.next_op or EmptyOperation() 
            else:
                current = current.next_op

        return copy_op 


    def calculate(self):

        # Multiplicação e Divisão
        updated_operation = self.calculate_priority_op()

        # Soma e subtração
        result = updated_operation.num
        current = updated_operation.next_op

        while current:

            if current.op == '+':
                result += current.num
            elif current.op == '-':
                result -= current.num

            current = current.next_op

        print("\nFinal result:", result)


           


class EmptyOperation:
    """Represents an empty operation (base case)."""

    def pp(self):
        print("()", end="")