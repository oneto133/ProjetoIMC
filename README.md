# Calculadora de IMC

Este projeto é uma calculadora simples de Índice de Massa Corporal (IMC). Ela permite que o usuário insira seu peso e altura e calcula o IMC, fornecendo uma classificação de acordo com os valores de referência da OMS.


**Tecnologias utilizadas:**

* Python
* Bibliotecas padrão do Python


**Como executar:**

1. Clone este repositório:
```
https://github.com/oneto133/ProjetoIMC.git
```
3. Instale as dependências:
```
pip install -r requirements.txt
```

4. Execute o script:
```
python Main.py
```


**Testes**

* Esse script foi feito em um conjunto de plataformas, tendo inicio no Google Cloud Shell
prosseguindo com testes unitários no Google Colab e fazendo a limpeza nescessária no Visual
Stúdio Code.

* Os Testes finais foram executados em terminaisn windows e linux(Ambiente virtual)
usado editores de códigos para testes como Jupyter e Pycharm para se certificar da qualidade
do código.

* Muitos desses testes apresentaram diferentes erros e apartir da identificação dos mesmos foram
feitas as alterações nescessárias para se obter o mínimo de inconveniente ao executar e usar do
programa.

* Alguns dos erros encontrados só poderaã ser corrigidos futuramente com implementação de um módulo
de configuração onde o usuário poderar fazer as alterações para se obter a melhor usabilidade possível.
Assim como muitas limitações do código, só deverão ter melhorias ao implementar um banco de dados, para
se obter um melhor controle dos dados e uma melhor experiencia do usuário, pois ao poder guardar e
gerenciar seus dados, o mesmo conseguirar ter um controle sobre sua saúde.


## Funcões

* O programa inicia fornecendo a hora para o usuário, horário padrao alinhado com a cidade de são paulo. Em seguida fornece dados de exemplo de entrada que serão aceitos, dados como strings não serão aceitos, com exceções das palavras-chaves como `Voltar` e `Sair` que em qualquer momento de recebimento de dados poderão ser inseridas para fazer alterações no andamento do programa.


**IMC**

* Com os dados Fornecidos, o calculo se inica passando por um tratamento, primeiro dados são checado, se puderem ser convertidos para float, passa por um tratamento de limite de peso, o peso máximo a ser recebido não pode ultrapassar `600 kgs`, assim como a altura não pode passar de `3 Metros`, após a verificação e com todos os dados certos, se dá início ao cálculo IMC.

* Após o resultado dos dados, é apresentado a situação do paciente de acordo com os dados fornecidos pela [OMS](https://aps.bvs.br/apps/calculadoras/?page=6)


**Continuar ou Finalizar?**

* Há uma entrada de dados com as opções de resposta entre **Sim** ou **Não** para o usuário decidir se quer continuar ou não. Uma verificação simples com uma limpeza de terminal que interage com alguns sistemas, como `Windows`, `Linux` e `Mac`.

### Considerações finais

* O código foi inteiro escrito de forma autêntica, assim como está documentado o uso do quadro kanban
no Trello. Foi usada de conceitos da metodologia ágil, incluindo o método incremental, onde, coforme
o projeto vai evoluindo, tambem vai sendo incrementado novos requisitos.

