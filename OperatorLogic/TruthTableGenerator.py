import argparse
from enum import Enum
from typing import List, Any
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
import sys

class Operation(Enum):
    """Available logical operations for multiple variables"""
    AND = "AND"
    OR = "OR"
    XOR = "XOR"  
    NAND = "NAND"
    NOR = "NOR"
    MAJORITY = "MAJORITY"
    PARITY = "PARITY"
    ALL_EQUAL = "ALL_EQUAL"

class MultiVariableBooleanComparator:
    """Boolean logic comparator using *args for unlimited variables"""
    
    def __init__(self):
        self.console = Console()
    
    # ==================== METHOD OVERLOADING WITH *args ====================
    
    def and_op(self, *values: bool) -> bool:
        """AND: All values must be True - works with any number of arguments"""
        return all(values)
    
    def or_op(self, *values: bool) -> bool:
        """OR: At least one value must be True - works with any number of arguments"""
        return any(values)
    
    def xor_op(self, *values: bool) -> bool:
        """XOR: Odd number of True values - works with any number of arguments"""
        return sum(values) % 2 == 1
    
    def nand_op(self, *values: bool) -> bool:
        """NAND: NOT AND - works with any number of arguments"""
        return not all(values)
    
    def nor_op(self, *values: bool) -> bool:
        """NOR: NOT OR - works with any number of arguments"""
        return not any(values)
    
    def majority_op(self, *values: bool) -> bool:
        """MAJORITY: True if more than half are True - works with any number of arguments"""
        if len(values) == 0:
            return False
        return sum(values) > len(values) / 2
    
    def parity_op(self, *values: bool) -> bool:
        """PARITY: True if odd number of True values - works with any number of arguments"""
        return sum(values) % 2 == 1
    
    def all_equal_op(self, *values: bool) -> bool:
        """ALL_EQUAL: True if all values are the same - works with any number of arguments"""
        if len(values) == 0:
            return True
        return len(set(values)) == 1
    
    # ==================== OPERATION DISPATCHER ====================
    
    def evaluate_operation(self, operation: Operation, *values: bool) -> bool:
        """
        Evaluate operation with unlimited boolean arguments using *args
        
        Args:
            operation: The logical operation to perform
            *values: Any number of boolean values
            
        Returns:
            Result of the logical operation
        """
        operations_map = {
            Operation.AND: self.and_op,
            Operation.OR: self.or_op,
            Operation.XOR: self.xor_op,
            Operation.NAND: self.nand_op,
            Operation.NOR: self.nor_op,
            Operation.MAJORITY: self.majority_op,
            Operation.PARITY: self.parity_op,
            Operation.ALL_EQUAL: self.all_equal_op
        }
        
        if operation not in operations_map:
            raise ValueError(f"Unsupported operation: {operation}")
        
        return operations_map[operation](*values)
    
    # ==================== DISPLAY METHODS ====================
    
    def compare_single_set(self, operations: List[Operation], *values: bool) -> None:
        """
        Compare single set of values with multiple operations using *args
        
        Args:
            operations: List of operations to apply
            *values: Any number of boolean values
        """
        if not values:
            self.console.print("[red]No values provided![/red]")
            return
            
        table = Table(
            title=f"🔍 Evaluating {len(values)} Variables: {list(values)}",
            title_style="bold blue",
            box=box.ROUNDED,
            show_header=True,
            header_style="bold magenta"
        )
        
        # Add columns for each variable
        for i in range(len(values)):
            table.add_column(f"V{i+1}", justify="center", style="cyan", width=6)
        
        table.add_column("Operation", justify="center", style="yellow", width=12)
        table.add_column("Formula", justify="center", style="white", width=25)
        table.add_column("Result", justify="center", style="bold", width=8)
        
        for operation in operations:
            result = self.evaluate_operation(operation, *values)
            
            row_data = []
            # Add variable values
            for value in values:
                row_data.append(f"[green]T[/green]" if value else f"[red]F[/red]")
            
            # Add operation
            row_data.append(operation.value)
            
            # Add formula
            values_str = " ".join("T" if v else "F" for v in values)
            formula = f"{operation.value}({values_str})"
            row_data.append(formula)
            
            # Add result
            row_data.append(f"[bold green]T[/bold green]" if result else f"[bold red]F[/bold red]")
            
            table.add_row(*row_data)
        
        self.console.print(table)
    
    def compare_multiple_sets(self, operation: Operation, *variable_sets) -> None:
        """
        Compare multiple sets of variables with single operation using *args
        
        Args:
            operation: Single operation to apply to all sets
            *variable_sets: Any number of variable sets (each set is a list/tuple of bools)
        """
        if not variable_sets:
            self.console.print("[red]No variable sets provided![/red]")
            return
        
        # Convert to lists if needed
        sets = [list(s) if not isinstance(s, list) else s for s in variable_sets]
        
        if not sets:
            self.console.print("[red]No valid sets found![/red]")
            return
            
        max_vars = max(len(s) for s in sets)
        
        table = Table(
            title=f"🔍 Comparing {len(sets)} Sets with {operation.value}",
            title_style="bold blue",
            box=box.HEAVY,
            show_header=True,
            header_style="bold magenta"
        )
        
        table.add_column("Set #", justify="center", style="white", width=6)
        
        # Add columns for each variable (based on max variables)
        for i in range(max_vars):
            table.add_column(f"V{i+1}", justify="center", style="cyan", width=6)
        
        table.add_column("Formula", justify="center", style="white", width=20)
        table.add_column("Result", justify="center", style="bold", width=8)
        
        for idx, values in enumerate(sets, 1):
            if not values:
                continue
                
            result = self.evaluate_operation(operation, *values)
            
            row_data = [str(idx)]
            
            # Add variable values (pad with empty for shorter sets)
            for i in range(max_vars):
                if i < len(values):
                    value = values[i]
                    row_data.append(f"[green]T[/green]" if value else f"[red]F[/red]")
                else:
                    row_data.append("-")
            
            # Add formula
            values_str = " ".join("T" if v else "F" for v in values)
            formula = f"{operation.value}({values_str})"
            row_data.append(formula)
            
            # Add result
            row_data.append(f"[bold green]T[/bold green]" if result else f"[bold red]F[/bold red]")
            
            table.add_row(*row_data)
        
        self.console.print(table)
    
    def demonstrate_with_examples(self) -> None:
        """Demonstrate the *args functionality with various examples"""
        console = Console()
        
        console.print(Panel.fit("[bold green]Demonstration of *args Functionality[/bold green]"))
        
        # Example 1: 2 variables
        console.print("\n[bold yellow]Example 1: 2 Variables[/bold yellow]")
        self.compare_single_set([Operation.AND, Operation.OR, Operation.XOR], True, False)
        
        # Example 2: 5 variables  
        console.print("\n[bold yellow]Example 2: 5 Variables[/bold yellow]")
        self.compare_single_set([Operation.MAJORITY, Operation.PARITY], True, False, True, True, False)
        
        # Example 3: 10 variables
        console.print("\n[bold yellow]Example 3: 10 Variables[/bold yellow]")
        self.compare_single_set(
            [Operation.AND, Operation.OR, Operation.MAJORITY], 
            True, False, True, False, True, True, False, True, False, True
        )
        
        # Example 4: Multiple sets comparison
        console.print("\n[bold yellow]Example 4: Multiple Sets with MAJORITY[/bold yellow]")
        self.compare_multiple_sets(
            Operation.MAJORITY,
            [True, False, True],           # 3 variables
            [True, True, False, True],     # 4 variables  
            [False, False, True, True, True]  # 5 variables
        )
    
    def show_operation_info(self) -> None:
        """Display information about available operations"""
        table = Table(
            title="📚 Available Operations (work with any number of variables)",
            title_style="bold green",
            box=box.DOUBLE,
            show_header=True,
            header_style="bold yellow"
        )
        
        table.add_column("Operation", style="cyan", width=15)
        table.add_column("Description", style="white", width=40)
        table.add_column("Example: op(T,F,T,F)", style="magenta", width=20)
        
    
        
    operation_descriptions = {
            Operation.AND: "All values must be True",
            Operation.OR: "At least one value must be True", 
            Operation.XOR: "Odd number of True values",
            Operation.NAND: "NOT(All values are True)",
            Operation.NOR: "NOT(Any value is True)",
            Operation.MAJORITY: "More than half are True",
            Operation.PARITY: "Odd number of True values (same as XOR)",
            Operation.ALL_EQUAL: "All values are the same"
        }
        
        

def parse_boolean_list(bool_string: str) -> List[bool]:
    """Parse comma-separated boolean values"""
    try:
        values = []
        for item in bool_string.split(','):
            item = item.strip().lower()
            if item in ['true', 't', '1', 'yes']:
                values.append(True)
            elif item in ['false', 'f', '0', 'no']:
                values.append(False)
            else:
                raise ValueError(f"Invalid boolean value: {item}")
        return values
    except Exception as e:
        raise argparse.ArgumentTypeError(f"Error parsing boolean list: {e}")

def parse_operation(op_string: str) -> Operation:
    """Parse operation string"""
    try:
        return Operation(op_string.upper())
    except ValueError:
        valid_ops = [op.value for op in Operation]
        raise argparse.ArgumentTypeError(f"Invalid operation: {op_string}. Valid options: {valid_ops}")
    
    
# ==================== MAIN CLI INTERFACE EXAMPLE ====================
def main():
    parser = argparse.ArgumentParser(
        description="Multi-variable Boolean Comparator using *args",
        epilog="Example usage:\n"
               "  python TruthTableGenerator.py --values true,false,true --operations AND,OR,XOR\n"
               "  python TruthTableGenerator.py --sets \"true,false;false,true,true\" --operation MAJORITY\n"
               "  python TruthTableGenerator.py --demo\n"
               "  python TruthTableGenerator.py --info",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    
    group.add_argument('--values', '-v', 
                      type=parse_boolean_list,
                      help='Comma-separated boolean values (any quantity: true,false,true,...)')
    
    group.add_argument('--sets', '-s',
                      help='Semicolon-separated sets ("true,false;false,true,true;...")')
    
    group.add_argument('--demo', '-d',
                      action='store_true',
                      help='Show demonstration with various examples')
    
    group.add_argument('--info', '-i',
                      action='store_true',
                      help='Show information about available operations')
    
    parser.add_argument('--operations', '-ops',
                       help='Comma-separated operations (AND,OR,XOR,...)')
    
    parser.add_argument('--operation', '-op',
                       type=parse_operation,
                       help='Single operation for multiple sets')
    
    args = parser.parse_args()
    
    comparator = MultiVariableBooleanComparator()
    console = Console()
    
    try:
        if args.demo:
            # Show demonstrations
            comparator.demonstrate_with_examples()
            
        elif args.info:
            # Show operation information
            comparator.show_operation_info()
            
        elif args.values:
            # Single set with multiple operations using *args
            if not args.operations:
                console.print("[red]Error: --operations required when using --values[/red]")
                sys.exit(1)
                
            operations = []
            for op_str in args.operations.split(','):
                operations.append(parse_operation(op_str.strip()))
            
            console.print(Panel.fit("[bold blue]Single Set, Multiple Operations (*args)[/bold blue]"))
            comparator.compare_single_set(operations, *args.values)
            
        elif args.sets:
            # Multiple sets with single operation using *args
            if not args.operation:
                console.print("[red]Error: --operation required when using --sets[/red]")
                sys.exit(1)
            
            variable_sets = []
            for set_str in args.sets.split(';'):
                variable_sets.append(parse_boolean_list(set_str.strip()))
            
            console.print(Panel.fit("[bold blue]Multiple Sets, Single Operation (*args)[/bold blue]"))
            comparator.compare_multiple_sets(args.operation, *variable_sets)
            
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        sys.exit(1)

if __name__ == "__main__":
    main()
'''
 =================================================================================================
  - Obviously  you can create diferens new files and directories for improve the project structure
       - but for simplicity I put all the code in a single file
  - You can run the script with --help to see usage 
=================================================================================================  
'''    