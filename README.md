# Criptografia: Protegendo suas informações com segurança

A criptografia é uma técnica fundamental para proteger informações confidenciais de acessos não autorizados. Ela consiste em converter dados legíveis em um formato ilegível, chamado de cifra, por meio de algoritmos matemáticos. Essa cifra só pode ser revertida para sua forma original por aqueles que possuem a chave de descriptografia adequada.

A história da criptografia remonta a milhares de anos, sendo usada desde tempos antigos por militares, diplomatas e governos para enviar mensagens secretas. Hoje em dia, a criptografia desempenha um papel essencial em nossas vidas digitais, protegendo transações bancárias, comunicações online, informações de identificação pessoal e muito mais.

Existem dois tipos principais de criptografia: simétrica e assimétrica. Na criptografia simétrica, a mesma chave é usada tanto para criptografar quanto para descriptografar os dados. Já na criptografia assimétrica, são usadas duas chaves diferentes: uma pública e outra privada. A chave pública é compartilhada com qualquer pessoa, enquanto a chave privada é mantida em segredo pelo destinatário das mensagens.

Além de garantir a confidencialidade dos dados, a criptografia também é essencial para garantir a integridade e autenticidade das informações. Ela impede que os dados sejam alterados ou adulterados durante a transmissão e verifica se o remetente é realmente quem ele afirma ser.

No entanto, é importante ressaltar que a segurança da criptografia depende da robustez dos algoritmos utilizados e do armazenamento seguro das chaves. Com o avanço da tecnologia, é necessário constantemente atualizar e aprimorar os métodos de criptografia para enfrentar novas ameaças e desafios de segurança cibernética.

Em resumo, a criptografia desempenha um papel crucial na proteção da privacidade e segurança dos nossos dados digitais em um mundo cada vez mais conectado. Ao garantir que apenas pessoas autorizadas possam acessar informações sensíveis, ela nos permite aproveitar os benefícios da tecnologia sem comprometer nossa segurança pessoal e privacidade.

# Criptografia Simétrica e Assimétrica

Este repositório contém exemplos de implementação de criptografia simétrica e assimétrica em Python, utilizando as bibliotecas `cryptography` para criptografia simétrica e `pycryptodome` para criptografia assimétrica.

## Pré-requisitos

Certifique-se de ter o Python instalado no seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

## Instalação

Para instalar as dependências necessárias, você pode usar o `pip`. Abra um terminal na raiz do projeto e execute os seguintes comandos:

```bash
pip install cryptography
pip install pycryptodome
pip install tk
```
## Cifra de Cesar
Para executar o exemplo da cifra de cesar, execute o seguinte comando:

```bash
caesarCipher.py
```

## Criptografia Simétrica
Para executar os exemplos de criptografia simétrica, execute o seguinte comando:

```bash
python symmetric_crypto.py
```

Este script demonstrará como criptografar e descriptografar mensagens utilizando criptografia simétrica.

##Criptografia Assimétrica
Para executar os exemplos de criptografia assimétrica, execute o seguinte comando:

```bash
python asymmetric_crypto.py
```

Este script mostrará como usar criptografia assimétrica para criptografar e descriptografar mensagens.

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver alguma melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request.


