from django.shortcuts import render


def index(request): 
    return render(request, 'dashboard/index.html')

# Auth
def login(request):
	return render(request, 'dashboard/login.html')

def forgot_password(request): 
    return render(request, 'dashboard/forgot-password.html')


# Monitoramento
def servicos(request):
	return render(request, 'dashboard/servicos.html')

def operacoes_monitoramento(request):
	return render(request, 'dashboard/operacoes_monitoramento.html')

def recebimento_de_dados(request):
	return render(request, 'dashboard/recebimento_de_dados.html')


# Cadastros
def contatos(request):
	return render(request, 'dashboard/contatos.html')

def clientes(request):
	return render(request, 'dashboard/clientes.html')

def modal(request):
    	return render(request, 'hx/modal.html')

def seguradoras(request):
	return render(request, 'dashboard/seguradoras.html')

def contratos(request):
	return render(request, 'dashboard/contratos.html')

def operacoes_cadastros(request):
	return render(request, 'dashboard/operacoes_cadastros.html')

def auxiliares(request):
	return render(request, 'dashboard/auxiliares.html')


# Financeiro
def notas_fiscais(request):
	return render(request, 'dashboard/notas_fiscais.html')

def faturamento(request):
	return render(request, 'dashboard/faturamento.html')

def reembolso(request):
	return render(request, 'dashboard/reembolso.html')

def budget(request):
	return render(request, 'dashboard/budget.html')


# Admin Sistema
def usuarios(request):
	return render(request, 'dashboard/usuarios.html')

def perfis(request):
	return render(request, 'dashboard/perfis.html')
