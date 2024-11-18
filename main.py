import os;

def limpar_console() -> None:
  if os.name == "nt":
    os.system("cls");
  elif os.name == "posix":
    os.system("clear");

def valida_input_menu_opcoes() -> int:
  while True:
    opcao_escolhida: str = input("> ");
    try:
      opcao_convertida_para_int: int = int(opcao_escolhida);
      if(opcao_convertida_para_int >= 1 and opcao_convertida_para_int <= 3):
        ativa_opcao_selecionada(opcao_convertida_para_int);
        return opcao_convertida_para_int;
      else:
        print("Digite um numero que seja uma das opçoes disponiveis");
        print("");
    except ValueError:
      print(f"Essa não é uma opção valida. Código do erro: {ValueError}"); 

def ativa_opcao_selecionada(opcao_selecionada: int) -> None:
  if opcao_selecionada == 1:

    print(f"A opção escolhida foi: {opcao_selecionada} (Compactar um arquivo)");

    nome_arquivo_para_compactar: str = input('''
Digite o nome do arquivo que deseja compactar
(Ex: meuArquivo.txt / arquivo_de_texto.txt / Exemplo.txt)
    ''');

    if not os.path.exists(nome_arquivo_para_compactar):
      print(f''''
O arquivo que voce escolheu não foi encontrado. Verifique as seguintes possibilidades:
- O arquivo não existe no mesmo diretório do programa (precisam estar na mesma pasta);
- O nome do arquivo pode ter sido digitado errado;
- Verifique se colocou a extensao do arquivo .txt;
      ''');
      return
    
    with open(nome_arquivo_para_compactar, 'r', encoding='utf-8') as arquivo:
      texto_extraido_do_txt: str = arquivo.read();

    texto_compactado: str = compactacao(texto_extraido_do_txt);

    nome_arquivo_compactado: str = input("Como deseja chamar o novo arquivo .txt compactado ?: ");

    with open(nome_arquivo_compactado, 'w', encoding='utf-8') as arquivo:
      arquivo.write(texto_compactado);

    print(f"Novo arquivo compactado foi salvo em {nome_arquivo_compactado}");
  
  elif opcao_selecionada == 2:
    print(f"A opção escolhida foi: {opcao_selecionada} (Descompactar um arquivo)");
    
    nome_arquivo_para_descompactar: str = input('''
Digite o nome do arquivo que deseja descompactar
(Ex: compactado.txt / arquivo_de_texto.txt / meuExemplo.txt)
    ''');

    if not os.path.exists(nome_arquivo_para_descompactar):
      print(f''''
O arquivo que voce escolheu não foi encontrado. Verifique as seguintes possibilidades:
- O arquivo não existe no mesmo diretório do programa (precisam estar na mesma pasta);
- O nome do arquivo pode ter sido digitado errado;
- Verifique se colocou a extensao do arquivo .txt;
      ''');
      return
    
    with open(nome_arquivo_para_descompactar, 'r', encoding='utf-8') as arquivo:
      texto_extraido_do_txt: str = arquivo.read();

    texto_descompactado: str = descompactacao(texto_extraido_do_txt);

    nome_arquivo_descompactado: str = input("Como deseja chamar o novo arquivo .txt descompactado ?: ");

    with open(nome_arquivo_descompactado, 'w', encoding='utf-8') as arquivo:
      arquivo.write(texto_descompactado);

    print(f"Novo arquivo compactado foi salvo em {nome_arquivo_descompactado}");
    
  elif opcao_selecionada == 3:
    print("Fechando o programa...");
  
def compactacao(texto: str) -> str:
  if not texto:
    return "";

  resultado: list = [];
  contador: int = 1;

  for indice in range(1, len(texto)):
    if texto[indice] == texto[indice - 1]:
      contador += 1;
    else:
      if contador >= 4:
        resultado.append(f"#{contador}{texto[indice - 1]}");
      else:
        resultado.append(texto[indice - contador:indice]);
      contador = 1;

  if contador >= 4:
    resultado.append(f"#{contador}{texto[-1]}");
  else:
    resultado.append(texto[-contador:]);
  return ''.join(resultado);

def descompactacao(texto_compactado: str) -> str:
  texto_descompactado: str = "";
  indice: int = 0;

  while indice < len(texto_compactado):
    if texto_compactado[indice] == '#':
      indice += 1;
      numero_hash: int = 0;

      while indice < len(texto_compactado) and texto_compactado[indice].isdigit():
        numero_hash: int = numero_hash * 10 + int(texto_compactado[indice]);
        indice += 1;
      
      caractere_compactado: str = texto_compactado[indice];
      indice += 1;

      texto_descompactado += caractere_compactado * numero_hash;
    else:
      texto_descompactado += texto_compactado[indice];
      indice += 1;
  return texto_descompactado;


limpar_console();
print("");
print('''

-- Compactação por Run Lenght --

Escolha o que deseja fazer:  
1 - Compactar um arquivo.
2 - Descompactar um arquivo.
3 - Sair.
''');
valida_input_menu_opcoes();