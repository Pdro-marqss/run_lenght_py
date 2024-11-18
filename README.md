**Menu de tópicos dessa documentação:**

Clique em uma para ir direto ao tópico.
- [O que é o algoritmo de compressao Run Lenght ?](#algoritmo-de-compressão-run-lenght)
- [Explicando o código](#falando-de-código)
  - [Tipagem de dados](#tipagem-de-dados)
    - [Como usar tipagem](#tipagens-primitivas-mais-usadas-no-código-e-como-tipar)
  - [Funções do programa](#funcões-do-programa)
    - [def limpar_console](#limpar_console)
    - [def valida_input_menu_opcoes](#valida_input_menu_opcoes)
    - [def ativa_opcao_selecionada](#ativa_opcao_selecionada)
    - [def compactacao](#compactacao)
    - [def descompactacao](#descompactacao)
  - [Execuções Base do programa](#execuçoes-base)

<br>
<br>

# Algoritmo de compressão "Run Lenght"
Esse Algoritmo serve para comprimir dados em caracteres (strings) que se repetem multiplas vezes seguidas. Por exemplo, se temos um texto que repete o caractere A 12 vezes, ao inves de escrever AAAAAAAAAAA, o metodo de compressao utiliza de um hash # seguido do numero de vezes que a letra se repete, e depois a propria letra **(#A12)**. Isso economiza espaço de memória que seria gasto com esses 12 A`s e agora são só 4 caracteres.

Vi algo sobre esse método ser muito utilizado antigamente em jogos, ja que o bitmap das cores na epoca era limitado e por isso repetia muito o código delas, entao esse algoritimo era super util pra reduz tamanho dos arquivos dos jogos.

Se quiserem saber mais sobre essa parte teórica eu recomendo darem uma olhada por aqui:
[Video YouTube - Ele explica legal mas usa jogo de MegaDrive na compressao](https://www.youtube.com/watch?v=GC8199jlkjs)

<br>

## Falando de código
Referente ao código, fiz ele em um esquema de "mini sistema". Então tem um sisteminha de interação do usuario onde ele seleciona através de uma menu, qual função do compactador ele quer usar. 

No total são 3 opçoes no menu (1- Compactar, 2- Descompactar e 3- Sair);

O código esta dividido em funcões principais (posicionadas na parte superior do código), e execuçao basica (a parte final).

Não coloquei a lógica em um loop, o que deixaria o programa rodando até o usuario clicar em sair. Isso adicionaria um tempinho a mais de desenvolvimento pra nao deixar pontas soltas e fazer um loop agradável. Não dei muita atenção pra esse capricho (perdão).

### Tipagem de dados
Usei aqui a tipagem de dados pra facilitar leitura do código, evitar erros e seguir boas práticas. A Tipagem de dados é quando, ao declarar uma variavel, eu digo qual o tipo de dado ela aceita ser. Por exemplo, como o python é uma linguagem com tipagem dinâmica, eu posso fazer: 
```py
nome = 123
idade = "Pedro"
conexao_wifi = "pedro3g"
wifi = 13556343245
```
Quando fica sem tipagem a leitura do código exige um tempo a mais pra identificar em certas partes (nem tanto na declaracao, mas ao longo do código) qual o tipo daquele dado, sendo que as vezes só o nome não ajuda muito a saber. Por exemplo o **conexao_wifi**... O nome nao me deixa claro se isso vai ser o nome da conexao em **string**, ou a senha dela em **string**, ou o id da rede em **int**... Nao da pra saber. O fato de usar tipagem nela, facilita nessas horas. Principalmente em **parametro de funcao**, quando uma funcao exige um parametro que voce vai usar pra somar com outro numero. Se eu nao souber que o que a funcao precisa é de um numero, posso tranquilamente passar uma **string** la, e quando for executar o código vai dar erro por tentar somar **string** com numero. ENFIM. Ta tipadinho ai gente.

#### Tipagens primitivas mais usadas no código e como tipar:
```py
#Pra tipar um dado, basta na declaracao da variavel a gente informar qual o tipo dela usando dois pontos seguido do nome do tipo.
nome: str = "Pedro"
idade: int = 25
altura: float = 1.83
is_dono_de_empresa: bool = False

#O tipo list é uma lista, mas podemos definir de que tipo essa lista é. Nesse caso abaixo, é uma lista do tipo string. Uma lista feita de strings
jogos_prediletos: list[str] = ['Cyberpunk 2077', 'Bioshock', 'Red Dead Redemption 2']

#também tem o tipo None, que representa um valor vazio, nulo ou indefinido. Usamos gearamente para tipar funcoes que não tem um retorno. 
def funcao_que_printa_na_tela() -> None:
  print("Como eu nao devolvo bosta nenhuma, é retorno None")

#Tipando parametros pra saber o que essa funcao espera receber e depois o que ela devolve.
def funcao_que_soma_e_devolve_valor_somado(valor1: int, valor2: int) -> int:
  print("Eu somo dois valores e te devolvo o resultado deles")
   return valor1 + valor2
```

<br>

### Funcões do programa:
#### limpar_console()
```py
def limpar_console() -> None:
  if os.name == "nt":
    os.system("cls");
  elif os.name == "posix":
    os.system("clear");
```
Usando o import de **OS** *(Que cuida de funcoes base do sistema operacional como ler, escrever em arquivos, obter dados de pastas ou nomes chaves do sistema, etc)*, eu verifico qual o nome do os ```os.name``` e verifico se ele é igual a **"nt"** ou **"posix"**. **Nt** significa **New Tecnology**, e é o nome adotado pelo **Windows** para sua **familia de sistemas operacionais (windows NT)**. Entao todos de lá pra ca, ao buscar o nome do os usando esse código python, retornam **NT**. Já o **posix** significa **Portable Operating System Interface**, e é usado em sistemas operacionais do tipo **UNIX**. Por isso sistemas **linux, Unix ou macOS** vao ter esse nome de os.

Sendo assim esse código valida se estamos em um **sistema windows** ou em um **sistema Unix** para definir qual o comando de limpar tela que vamos usar. Em **powerShell (windows)**, usamos o comando de prompt **"cls"** para limpar tela. Já em prompt **unix**, usamos o **"clear"**.

Referente a tipagem, o retorno dessa funcao é do tipo ```None```, já que ela não me retorna nenhum valor. Apenas executa o que tem que fazer e já era.

<br>

---

#### valida_input_menu_opcoes()
```py
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
```
Aqui nós validamos **se o que o usuário está digitando é um input valido para o menu de opçoes**. Como o menu tem 3 opcões que são escolhidas baseadas no numero de 1 a 3, não podemos aceitar um input do usuario que seja uma letra do alfabeto, caracteres especiais ou numeros que sao menores que 1 ou maiores que 3.

Então aqui primeiro definimos o retorno da funcao como ```int```, para dizer que ao final, essa funcao deve retornar um valor **inteiro** como resultado. Esse valor sera a opcao escolhida pelo usuario.
```py
def valida_input_menu_opcoes() -> int:
```

Depois criamos um laço ```while``` pra gerar um **loop de execução**. Aqui a ideia é fazer a funcão rodar enquanto o usuario não digitar um comando valido, gerando aquele loop de *"opcao invalida, tente novamente"*, sabe ?

Então criamos uma variavel ```opcao_escolhida ``` que é do tipo string e tem seu valor definido por um input do usuario, que sera a opção que ele escolheu.
```py
while True:
    opcao_escolhida: str = input("> ");
```
Logo abaixo iniciamos um **TRY CATCH** *(no python é chamado de **TRY EXCEPT**, mas funciona igual ao try catch de outras linguagens)*, onde dividimos a operaçao em 2 blocos. O bloco de ```TRY``` é onde **TENTAMOS** fazer alguma coisa, nesse caso, tentamos converter o input do usuario para o tipo **INT** *(ja que todo input em python é recebido como **string**, precisamos tratar pro tipo desejado depois, nesse caso, um **inteiro** que representa 1, 2 ou 3)* e validamos se o numero é ```< ou igual a 1, ou > ou igual a 3```. Caso seja, ele ativa a função de ```ativa_opcao_selecionada()``` *(Que sera explicada em breve)*, passando como parametro dela, o numero da opção que o usuário selecionou, ja que agora temos esse numero tratado e validado.
```py
try:
  opcao_convertida_para_int: int = int(opcao_escolhida);
  if(opcao_convertida_para_int >= 1 and opcao_convertida_para_int <= 3):
    ativa_opcao_selecionada(opcao_convertida_para_int);
    return opcao_convertida_para_int;
  else:
    print("Digite um numero que seja uma das opçoes disponiveis");
    print("");
```
**AGORA CASO O USUARIO DIGITE ALGO INVALIDO**, como uma letra ou um numero fora do range de validacao do bloco ```TRY```, o código é jogado no ```EXCEPT```, onde ele recebe naturalmente um ```valueError``` (um código genérico de erro que o próprio python da pra gente), e la eu passo um ```print()``` dizendo que o valor digitado nao é valido, junto ao código de erro padrao que foi emitido pelo ```EXCEPT```.
```py
except ValueError:
  print(f"Essa não é uma opção valida. Código do erro: {ValueError}");
```

Como a parte atual do código esta em loop, isso vai acontecer até o usuario digitar algo valido.

>**OBS:** Nesse ```TRY```, ele vai ser lançado diretamente ao ```EXCEPT``` quando o usuario digitar um letra porque a conversão de uma letra pra **int** nessa parte... : 
```py
opcao_convertida_para_int: int = int(opcao_escolhida);
``` 
>...gera um erro que normalmente pararia o código na hora... Literalmente interrompe a execucao dele e para de rodar... A utilidade do ```TRY EXCEPT``` é justamente tratar esse **erro** que iria interromper o código, armazenar ele no ```valueError``` e jogar o fluxo do código em outra direçao (que seria o ```EXCEPT```), evitando assim que sua execução seja travada. Então assim que o código tenta transformar uma letra ou dado invalido do usuario em um inteiro, ele joga voce no ```EXCEPT```. Belezinha???

<br>

---

#### ativa_opcao_selecionada()

Aqui vamos dividir por partes... Essa função recebe como parametro 1 valor chamado ```opcao_selecionada``` que é um ```int``` e tem como retorno da funcão ```None```, porque não retorna nenhum valor bruto dela, apenas executa código dentro do bloco.
```py
def ativa_opcao_selecionada(opcao_selecionada: int) -> None:
```

A primeira parte dessa função é caso o usuario tenha selecionado a ***opcao 1***. Aqui significa que ele escolheu ***COMPACTAR*** um arquivo, então temos um print basico que fala qual opcao foi escolhida, depois vamos a captura do ```INPUT``` do usuario, que sera o nome do arquivo que ele deseja compactar.
```py
if opcao_selecionada == 1:
  print(f"A opção escolhida foi: {opcao_selecionada} (Compactar um arquivo)");

  nome_arquivo_para_compactar: str = input('''
Digite o nome do arquivo que deseja compactar
(Ex: meuArquivo.txt / arquivo_de_texto.txt / Exemplo.txt)
  ''');
```

>Aqui precisamos nos atentar no nome do arquivo. Ele deve ser ***EXATAMENTE*** igual ao nome do arquivo que ***DEVE POR OBRIGATÓRIEDADE*** estar na mesma pasta do programa... ***na mesma raiz !!!*** Então se o arquivo com o texto a ser compactado se chama ***ai_bolçonaru.txt***, o nome digitado aqui deve ser exatamente esse... mas caso o usuario digite errado, já tratei alguns casos de erro aqui :)

Após receber o ```input``` do usuario que seria o nome do arquivo, usamos uma validaçao em ```NOT``` *(é o mesmo que o operador ```NOT``` **(!)** usado em outras linguagens)*, para verificar se o arquivo não for encontrado.. 

Essa validaçao em ```NOT``` é um fluxo oposto do ```IF``` normal... Geralmente a gente faz ```if numero > 2:``` e interpretamos isso como ```SE o numero digitado for MAIOR que 2, fazemos tal coisa:```, o que nos gera um ```TRUE``` ou ```FALSE```, ja que o retorno de um ``if`` é sempre um **booleano**... Todo if verifica a condiçao que descrevemos e retorna pra gente um **VERDADEIRO** caso a condicao seja verdadeira, ou **FALSE** caso nao seja. Então no exemplo do numero, vamos ter **TRUE** caso o **NUMERO** seja **maior** que **2**, e assim entramos no fluxo do **if**. Ja uma validaçao em ```NOT``` é negativa, ou seja, quando usamos ele, a leitura fica oposta ao fluxo padrão, então nao entramos mais no bloco de código caso a condicão seja verdadeiro, e sim se ela for ``FALSE``.

Voltando ao nosso código, nessa linha... 
```py
if not os.path.exists(nome_arquivo_para_compactar):
``` 
...verificamos se **NÃO** existe um caminho na raiz atual que tenha o nome que foi digitado pelo usuario. Caso ele não exista, exibimos um erro em ``print()`` explicando o erro e dando possiveis soluções para ele, e aplicamos um ``return`` para encerrar a execuçao do código, já que uma das causas pode ser arquivos faltando, é melhor encerrar nessa parte para evitar conflitos de arquivos do que manter um loop que deixe o programa rodando... Caso exista o arquivo digitado, seguimos com o fluxo do código para a próxima etapa.

<br>
<br>

**MANIPULANDO ARQUIVOS**

Aqui agora, vamos começar a **manipular arquivos** de fato, usando funcoes nativas do python como o ```open()```. Essa funcao aceita alguns parametros, sendo eles:

**NOME_DO_ARQUIVO:** nome do arquivo que sera manipulado;

**TIPO DE MANIPULAÇÃO:** Se a manipulaçao sera uma **leitura (r)**, uma **escrita (w)**, ou outras possiveis.

**TIPO DO ENCODING:** Qual encoding de caracterers serao usados. No nosso caso é o **UTF-8** (que representa caracteres especiais e de todos os grandes idiomas. conhecido como UniCode)
```py
with open(nome_arquivo_para_compactar, 'r', encoding='utf-8') as arquivo:
```
O comando ``WITH`` que vem antes da chamada dessa funcao ``Open()`` é **MUITO IMPORTANTE**... Ele é chamado de **GERENCIADOR DE CONTEXTO**. Esse comando é usado em objetos e funcoes do python que precisam ser limpos depois de usados (como arquivos, conexoes de rede, dentre outros). Esse tipo de operaçao se inicia e começa a tomar recursos do computador pra se manter em uso, caso nao seja finalizada, corre o risco de demandar muito mais recursos do que o necessario, entao é importante sempre finalizar uma operacao dessas quando se termina o uso. Quando se inicia uma conexao de rede, em algum momento ela deve ser finalizada... Ou no nosso caso quando se abre um arquivo, seja pra leitura ou escrita, em algum momento precisamos fechar ele. 

Se a gente fosse fazer de forma manual ficaria mais ou menos assim: 
```py
#Abrindo o arquivo manualmente e atrelando a um espaço de memoria
arquivo = open('meuAquivo.txt', 'r');

#Lendo o conteudo do arquivo
conteudo = arquivo.read();

#Fechando o arquivo após o uso
arquivo.close();
```
Para evitar esquecimentos e trabalhar de uma forma mais otimizada, usamos o ``WITH`` que já fica responsavel por abrir e fechar o arquivo ao final da execuçao do bloco de código dentro dele.

O ``as arquivo`` que tem no final da linha de código, é uma forma alternativa de atribuir uma variavel... Estamos falando aqui que o resultado dessa abertura de arquivo fica salva em uma variavel chamada **Arquivo**. Mas é o mesmo que declarar uma variavel (como foi feito ali em cima na explicacao do metodo manual).

Terminadas as explicaçoes sobre essa parte, vamos voltar a execuçao do código logo após ele abrir o arquivo que o usuario digitou o nome no **input**. Agora vamos para a etapa de **extrair** o texto do arquivo e armazena-lo em uma variavel chamada **texto_extraido_do_txt**, que é o do tipo **String** e recebe o valor de ``arquivo.read()``, ou seja, recebe o valor do conteudo em **string** dentro do arquivo de texto.
```py
texto_extraido_do_txt: str = arquivo.read();
```

Abaixo temos a chamda da funcao principal do algoritmo, a funcao de **COMPACTAÇÃO**. Aqui nos criamos uma variavel chamada **"texto_compactado"**, que tem seu tipo definido como uma **string**, e atribuimos a ele o valor do retorno da funcao de compactacao, que recebe como parametro o texto que foi extraido do txt.
```py
texto_compactado: str = compactacao(texto_extraido_do_txt);
```

Antes de explicar a funcao de **compactacao** vamos finalizar esse bloco de código... Assumindo que o valor do texto extraido do arquivo foi passado como parametro na funcao de **compactacao**, e o valor da variavel **texto_compactado** agora é de fato o texto original só que compactado, vamos criar um arquivo para salvar esses valores compactados. Isso é feito na linha seguinte, onde perguntamos ao usuario qual o nome ele deseja dar ao novo arquivo que sera gerado com o valor da compactacao dentro. Esse nome é dado atraves de um ``INPUT``, e em seguida usamos uma linha de código semelhante a de leitura de arquivo, só que agora mudamos um parametro da funcao que antes era **'r' de read** para **'w' de write**. Agora estamos escrevendo em um novo documento de texto. Como esse documento provavelmente ainda não existe, o python vai criar um com o nome **EXATO** que foi descrito pelo ```input``` do usuario. Caso ja exista, ele vai substituir o velho pelo novo. Após isso um print é disparado avisando que o arquivo foi salvo e o nome dele...
```py
nome_arquivo_compactado: str = input("Como deseja chamar o novo arquivo .txt compactado ?: ");

  with open(nome_arquivo_compactado, 'w', encoding='utf-8') as arquivo:
    arquivo.write(texto_compactado);

  print(f"Novo arquivo compactado foi salvo em {nome_arquivo_compactado}");
```
>AQUI DARIA PRA FAZER UMA VALIDACAO A MAIS PRA VERIFICAR SEMPRE SE O USUARIO DIGITOU NO FINAL DO INPUT DELE O VALOR DE .TXT, CASO NAO TENHA, PODERIAMOS ADICIONAR MANUALMENTE, ASSIM REDUZIRIA O RISCO DE FALHAS POR ESQUECER DE DEFINIR O TIPO DO ARQUIVO... MAS AI É LUXO JÁ.

Agora na **SEGUNDA PARTE** dessa funcao, temos a escolha da **opcao 2**, que é a de **DESCOMPACTAÇÃO**... Quando forem ver essa parte, vão notar que ela é **extremamente similar** a primeira parte, tirando a funcao que é chamada (agora a de descompactar), e alguns detalhes como o nome do arquivo. O resto é muito semelhante (poderia e DEVERIA até ser uma funcao isolada. Se o código se repete mais de uma vez, provavelemente deveria ser uma funcão... mas como são 4 da manha e eu ainda tenho que temrinar essa documentação, vou deixar esse capricho pra aventuras futuras, meus amigos).

Dito isso, acho que não preciso me extender explicando a segunda opcao, ja que é quase um copia e cola.... A terceira opcao é só um ``print()`` de *"fechando o programa"* sem chamar nenhuma outra funcao, o que gera o fim dele.

<br>
<br>

---

**Vamos agora ao principal e talvez o mais dificil de entender. As funcoes de:**
#### Compactacao()
```py
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
```

A função de compactacao recebe um parametro **TEXTO** que é do tipo **string**, e tem como **retorno** da funcao, ou seja, resultado dela, uma **string** também.
```py
def compactacao(texto: str) -> str:
```
Logo no inicio ja validamos ``NOT`` de texto. Se ali tivessemos só um ```if texto```, seria uma validacao se texto existe, se o valor que foi passado pelo parametro é um valor preenchido, e nao algo vazio... No caso da nossa validacao em ``NOT``, estamos vendo se **TEXTO NÃO É VAZIO**. Caso seja, ele retorna uma **string** vazia como resultado dessa funcao, ja que o texto que recebemos e que deveria ser o valor a ser compactado não existe, vamos retornar como resposta uma **string** vazia "".
```py
if not texto:
  return "";
```
Agora caso exista **TEXTO** e ele não seja vazio, seguimos com o código...

Abaixo da validacao, damos inicio a algumas **variaveis** de apoio na logica do algoritmo a seguir. A primeira delas e uma **lista** em **ARRAY** que vai armazenar o resultado final da **compactacao**, e o segundo é um **contador** que sera o repsonsavel por armazenar a contagem de quantos caracteres repetidos temos em cada validação.
```py
resultado: list = [];
contador: int = 1;
```
Seguindo, damos inicio ao laço ``FOR`` onde inicializamos um **indice** no **range** de 1 até o tamanho de caracteres presentes em **TEXTO**.
```py
for indice in range(1, len(texto)):
```
Depois verificamos se ``texto[indice]``, ou seja, o caratere atual do loop for em que estamos, é igual ao caractere anterior, ``texto[indice - 1]``... Por isso no ``FOR``, dentro do range começamos a contar a partir do 1 (ou seja, do segundo caractere) e nao do primeiro (que seria o 0)... porque nao tem como comparar o caractere 0 com o anterior, sendo que nao existe anterior. Entao começamos do segundo
```py
if texto[indice] == texto[indice - 1]:
```
Só pra deixar mais claro. Em PEDRO a contegem de indices é assim: P(indice 0) E(indice 1) D(indice 2) R(indice 3) O(indice 4). Não tem como eu comparar se P é igual ao caractere anterior, entao a comparacao pode começar do segundo caractere. Assim que é ali em cima.

Após verificarmos se o caractere atual é igual ao anterior, caso seja verdade, adicionamos + 1 ao **contador**, e continuamos no loop com o proximo caractere. 

Agora caso seja **FALSE** e o caractere atual nao seja igual ao anterior, consideramos que aquela sequencia de caracteres terminou, entao estamos prontos para validar se ela foi maior que 4, assim podemos comprimir esse conjunto de caracteres. Caso nao tenha sido maior que quatro nós só zeramos o **contador** e seguimos para o proximo caractere unico. Caso seja maior que 4 a gente faz um **append** *(adiciona um item ao final de uma lista, no nosso caso, a lista de resultados)* para adicionar o código referente a **compactacao** daquela sequencia de caracteres. Isso é feito usando o **hash #** seguido da quantidade salva em **contador** *(que representa quantas vezes aquele caractere foi repetido simultameneamente)*, e depois qual caractere era aquele. Formando assim o **hash #5A** (por exemplo).
```py
else:
  if contador >= 4:
    resultado.append(f"#{contador}{texto[indice - 1]}");
```
Caso o **contador** **nao seja maior que 4**, significa que a sequencia de caracteres nao precisa ser **comprimida**, entao ele só faz um **SLICE** pra verificar onde no texto aquele caractere começou a aparecer e onde terminou. Ele corta esse pedaço de texto e só faz o append dele na lista de **resultado**. Entao se tinhamos 3 letras Z ele só corta as 3 e cola no **append**.
```py
else:
  resultado.append(texto[indice - contador:indice]);
contador = 1;
```
Depois disso **reseta o contador** pra 1, indicando que aquela sequencia de caracteres terminou e agora vai começar a recontar a próxima.

**Após o loop principal**, verificamos se a **ultima sequencia de caracteres** também precisa ser **compactada**. Isso porque o **trigger** para salvar a sequencia compactadada, é quando o caracter seguinte nao é igual ao anterior, porém quando chegamos nos ultimos, nao temos essa validacao se o proximo depois dele é igual a ele. Entao usamos essa regra pra fechar o ciclo de vez.

A linha: ```resultado.append(texto[-contador:]);``` quer dizer que estamos anexando ao resultado, os caracteres que nao entraram na condicao de serem repetidos + de 4 vezes. Aqui a gente usa do indice negativo para usar o fatiamento a partir do final da string.

Por fim usamos o ``join`` para unificar a lista em uma string unica. Atualmente tinhamos um **ARRAY** com os valores compactados em cada posicao da lista. ``Resultado = ['#6A', 'CC', #7B]``... Depois do ``join`` vira uma **string** só. ``Resultado = '#6ACC#7B'``.
```py
if contador >= 4:
  resultado.append(f"#{contador}{texto[-1]}");
else:
  resultado.append(texto[-contador:]);
return ''.join(resultado);
```
<br>
<br>

---

#### Descompactacao()
O algoritmo de **descompactacao** é a **engenharia reversa do primeiro**. Aqui a gente vai verificar a nova string compactada e buscar pelos **hashes #** pra entao olhar o numero na frente deles. Armazenar esse numero em uma variavel. Olhar pro caractere na frente do numero. Armazenar esse caractere em uma variavel e entao multiplicar ele pelo numero. Entao saberemos quantas vezes cada caractere precisa aparecer.

Explicando com mais calma, essa funcao recebe um parametro chamado **"texto_compactado"** que é do tipo **string**. A funcao retorna um tipo **string** também, que é o resultado dela (A string do texto descompatado).
```py
def descompactacao(texto_compactado: str) -> str:
```
Logo no começo a gente cria 2 variaveis. A que vai **armazenar o resultado do texto descompactado** (e é do tipo **string**), e a de **indice que vai contar quantos valores temos compactados na string** (e é do tipo **int**). A varivavel do texto começa como vazia, ja que ainda nao descompactamos para salvar nela, e a segunda começa como 0.
```py
texto_descompactado: str = "";
indice: int = 0;
```
Criamos um loop ``WHILE`` que tem como condicao, enquanto **indice** for menor que o **tamanho de caracteres** que temos no **texto compactado**, que foi passado como parametro pra ativar essa funcao de descompactacao.
```py
while indice < len(texto_compactado):
```
A primeira condicao que temos é **SE** o **indice** atual de **texto_compactado** é uma **HASH**. Se for o caso, adicionamos **+1 ao indice** e criamos uma nova variavel chamada de **numero_hash** (que é um inteiro), que vai armazenar o numero seguido da **HASH**, ou seja, o numero que define quantas vezes aquele caractere se repete. Apos criar essa nova variavel inicalizamos ela como 0.
```py
if texto_compactado[indice] == '#':
  indice += 1;
  numero_hash: int = 0;
```
Em seguida inicamos outro bloco ``WHILE``, que vai funcionar **ENQUANTO** indice for menor que o tamanho de caracteres em **texto_compactado** E **ENQUANTO** o caractere atual sendo olhado for um digito de **0-9** *(mesmo que esteja em estado de string)*. A funcao ``isdigit()`` padrao do python serve para validar se um caractere em string **é um numero de 0 a 9**. Ele serve para validarmos se é um numero mesmo nao tendo convertido ele pra algum tipo numero ainda. Entao mesmo sendo uma **string** (texto), a funcao detecta que esse texto bate com um caractere de **0-9** e devolve **true** como resposta. Logo, nesse ``WHILE`` estamos vendo se **indice** é menor que a **quantidade de caracteres** que temos em **texto_compactado**, e se o caractere atual é um digito. Isso porque já identificamos onde esta a **HASH**, entao sabemos que depois dele vem um digito numero que simboliza a quantidade de vezes que aquele caractere se repete. Agora precisamos rodar esse loop ``WHILE`` até que o ele identifique um caratere que nao seja um ``isdigite()``, ou seja, deixa de ser um numero e volta a ser um caracrete qualquer, significando que aquela sequencia de caracteres iguais acabou.

Como a sequencia pode ser grande, como por exemplo 14 caracteres A **(#14A)**, precisamos formatar o dado para que ele identifique valores acima de 1 digito. Se na variavel **numero_hash** só atribuicemos o valor de ``texto_compactado[indice]``, estariamos salvando o primeiro numero encontrado, mas nao o segundo. Entao no caso do exemplo de **#14A** ficaria como **numero_hash** apenas o digito 1. No próximo loop do **while** ele reescreveria esse valor pelo segundo digito. Entao o valor de **numero_hash** seria 4. Assim ta errado. O que ele tem que fazer é identificar os digitos numeros e formar a partir deles o valor total. Pra isso usamos a seguinte logica:
```py
numero_hash: int = numero_hash * 10 + int(texto_compactado[indice]);
```
**Aqui pegamos o atual numero_hash * 10 + o digito numero seguinte seguinte.**

No exemplo **#14A** ficaria assim:

O valor de **numero_hash** sempre começa como 0. Entao no primeiro loop essa linha de código faria ```0 * 10 + 1``` que resulta em 1. Já no segundo loop, agora o valor de **numero_hash** é 1, então nessa volta do loop o calculo fica ```1[valor atual de numero_hash] * 10 + 4[valor do digito atual]``` que resulta em 14. Então essa linha de codigo basicamente gera o valor atual e caso necessario, movimenta o valor uma casa pro lado e adiciona o novo valor.

Logo após esse calculo ele incrementa o indice em valor atual + 1 e isso da sequencia ao proximo caractere do **texto_compactado**. Agora é a vez do Caractere em si, o que foi compactado... já achamos o **HASH #**, ja identificamos e formatados os **digitos da quantidade de vezes que o caractere repete**, e agora vamos **identificar qual é o caractere**. Pra isso criamos uma variavel chamada **caractere_compactado**, que é do tipo string, e recebe como valor o caractere do **indice** atual em que estamos *(já que pela ordem natual passamos por HASH, VALOR e agora no indice só pode ser ele)*. Após termos salvo o caractere, podemos seguir, etão incrementamos novamente o indice no seu valor atual + 1 para seguir para o próximo.
```py
caractere_compactado: str = texto_compactado[indice];
indice += 1;
```
Quando chegamos ao final de uma sequencia dessa **#HASH 14VALOR A-CARACTERE**, sabemos que um cilco terminou, então na linha seguinte vamos salvar na variavel **texto_descompactado** *(onde estamos salvador a string final do texto descompacatado)*, o valor que obtivemos até agora. No caso, vamos icrementar nele *(ou seja, pegar o valor que já tinha e só adiconar mais coisas depois)* o valor do caratere que capturamos em **caractere_compactado** * o numero de vezes que ele aparece **(numero_hash)**. Isso vai transformar o **#5A** em **AAAAA**.
```py
texto_descompactado += caractere_compactado * numero_hash;
```
Chegando no final do ``IF`` que verifica se o caractere era um **HASH #**, entramos no ``else``, caso o caratere não seja um **HASH**. Isso sigifica que é um caractere que nao foi **compactado**, ou seja, não precisou por ter uma sequencia abaixo de 4. Nesse caso vamos só adicionar a string de **texto_descompactado** incrementado seu valor atual com o caractere atual (que nao foi comprimido).
```py
else:
  texto_descompactado += texto_compactado[indice];
  indice += 1;
```
Ao final do processo aplicamos um return ao valor final que é o **texto_descompactado**. Nele já temos nosso **texto original** de volta.

<br>

---

### Execuçoes Base
Agora abaixo das **funcoes** temos a **execuçao base** do programa, que **são as chamadas dessas funcões criadas**...Não chamamos todas elas aqui porque algumas são ativadas em outras etapas de outras funcoes. Mas as que temos aqui são:

**O primeiro clean de console** pra caso o usuario ja tenha usado outras vez o programa. Isso impede a tela de ficar poluida.

**Um print("") vazio pra pular uma linha** do texto padrao do console do computador (coisa estetica, só pra ficar bonitinho)

``print()`` com o menu de opçoes base do programa

**Chamada do** ``valida_input_menu_opcoes()`` que é a primeira chamada relevante do sistema. Aqui a gente pede o input do usuario, apartir dele ativamos uma das opcoes possiveis e nessa ativaçao rodamos a compatacao, descompactacao ou saida do aplicativo.

<br>

---

>**É isso amigos... Espero ter ficado claro. Tentei deixar o mais explicativo possivel, mesmo achando que ficou coisa pra porra pra ler. Perdoem-me. Qualquer duvida me chamem !!!**
