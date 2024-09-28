import os
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import SQLFileForm
from .models import SQLFile
from .quantum_optimizer import create_quantum_circuit, visualize_circuit

def home(request):
    return redirect('upload_file')  

def optimize_sql(query):
    return query.strip() 

def upload_file(request):
    if request.method == 'POST':
        form = SQLFileForm(request.POST, request.FILES)
        if form.is_valid():
            sql_file = form.save()
            optimized_filename = f'optimized_{os.path.basename(sql_file.uploaded_file.name)}'
            optimized_path = os.path.join(settings.MEDIA_ROOT, 'optimized_files', optimized_filename)

            with open(sql_file.uploaded_file.path, 'r', encoding='utf-8') as f:
                original_queries = f.readlines()

            optimized_queries = [optimize_sql(query) + '\n' for query in original_queries]

            # Create and visualize the quantum circuit
            marked_index = 0  
            quantum_circuit = create_quantum_circuit(len(original_queries), marked_index)
            circuit_diagram = visualize_circuit(quantum_circuit)  

            # Save optimized SQL in a file
            with open(optimized_path, 'w', encoding='utf-8') as f:
                f.writelines(optimized_queries)

            sql_file.optimized_file = f'optimized_files/{optimized_filename}'
            sql_file.save()

            return render(request, 'result.html', {'sql_file': sql_file, 'circuit_diagram': circuit_diagram})
    else:
        form = SQLFileForm()

    return render(request, 'upload.html', {'form': form})

def result(request, sql_file_id):
    sql_file = SQLFile.objects.get(id=sql_file_id)
    circuit_diagram = request.POST.get('circuit_diagram', '')
    return render(request, 'result.html', {'sql_file': sql_file, 'circuit_diagram': circuit_diagram})
