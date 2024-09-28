from qiskit import QuantumCircuit

def create_quantum_circuit(n, marked_index):
    """
    Creates a Grover's search quantum circuit without executing it.
    
    Parameters:
    - n: number of qubits
    - marked_index: the index of the marked item (0-based)
    
    Returns:
    - A QuantumCircuit object representing Grover's search.
    """
    # Create a quantum circuit with n qubits
    circuit = QuantumCircuit(n)

    # Initialize the qubits to |+>
    for i in range(n):
        circuit.h(i)  # Apply Hadamard gate to each qubit

    # Flip the sign of the marked element
    circuit.z(marked_index)  # Apply Z gate to the marked index

    # Grover's diffusion operator
    circuit.h(range(n))
    circuit.x(range(n))
    
    # Since mct is not available, So implement Toffoli for 3 qubits
    if n >= 2:
        circuit.ccx(0, 1, n-1)  # Simple Toffoli gate
    if n > 2:
        circuit.ccx(1, 2, n-1)  # Additional Toffoli gate if n > 2

    circuit.h(range(n))
    circuit.x(range(n))

    return circuit

def visualize_circuit(circuit):
    """
    Visualizes the quantum circuit.
    
    Parameters:
    - circuit: QuantumCircuit object
    """
    return circuit.draw()  # Returns a text-based representation of the circuit
