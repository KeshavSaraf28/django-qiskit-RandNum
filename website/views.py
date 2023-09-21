from django.shortcuts import render,redirect
import numpy as np
from qiskit import QuantumCircuit,QuantumRegister,ClassicalRegister,execute
from qiskit import IBMQ,Aer,transpile,assemble
import math
# IBMQ.save_account('eb264c4a6d39359629fc0dd4d0031812fb511701c624409f3dd905af17e33f3d6d792b9b0b449b1931f1acdb2578aee7cde105c736e48c735e20603a378299c8',overwrite=True)
# provider = IBMQ.load_account()

def RandNumGenerator(min,max):
    if(min==max): 
        return min
    if(min>max):
        return RandNumGenerator(max,min)
    range_length=max-min;
    qubits_to_use=math.ceil(math.log2(range_length))
    bits=ClassicalRegister(qubits_to_use)
    qubits=QuantumRegister(qubits_to_use)
    circuit=QuantumCircuit(qubits,bits)
    for i in range(qubits_to_use):
        circuit.h(qubits[i])
    for i in range(qubits_to_use):
        circuit.measure(qubits[i],bits[i])
    backend=Aer.get_backend('qasm_simulator')
    job=execute(circuit,backend,shots=1)
    result=job.result()
    counts=result.get_counts()
    number=next(iter(counts))
    number=int(number,2)
    number=math.floor((number/((2**qubits_to_use)-1))*range_length)+min
    return number        

# Create your views here.
def home(request):
    if request.method == "POST":
        min=request.POST["min_number"]
        max=request.POST["max_number"]
        number=RandNumGenerator(int(min),int(max))
        return render(request, "home.html", {"number":number,'min':min,'max':max})
    else:
        return render(request, "home.html", {})