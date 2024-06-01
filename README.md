# Clínica Médica - Laboratório Dev. de Software

##  Objetivo
- Este projeto está sendo realizado para a disciplina de "Laboratório de Desenvolvimento de Software" utilizando o framework Django da linguagem Python.
- Consiste em um sistema web para agendamento de consultas médicas e gestão de usuários.


## Documentação da Ferramenta

- Todas as informações básicas e guias de uso da ferramenta Django estão presentes na documentação do mesmo
- https://docs.djangoproject.com/en/5.0/
</br>

## Escopo do projeto / Minimundo

 Em uma cidade pequena, existe apenas uma clínica médica para atender toda a população da cidade e constantemente tem de lidar com a superlotação de pacientes. Todos os pacientes necessitam passar por etapas de atendimento para que possam agendar consultas com médico especializado e passar pelo mesmo processo para cancelar estas consultas. Isso causa um grande congestionamento na    prestação desses serviços aos seus pacientes.

A clínica em questão deseja implementar um sistema web com o objetivo de agilizar  o cadastro dos dados dos pacientes, manter informações de contato e localização da clínica e facilitar o acesso dos pacientes aos serviços ofertados pelo hospital, agendar consultas com médico especializado, acompanhar o histórico de consultas e disponibilizar as informações dos profissionais disponíveis para atendimento aos pacientes.

O sistema permite que os pacientes se cadastrem no sistema. O paciente é caracterizado por um código único, nome completo, data de nascimento, CPF e deve fornecer email e senha para autenticar seu acesso ao sistema. Esses dados devem ser validados pelo próprio sistema, caso estejam incorretos, o processo de login (acesso ao sistema) deve ser realizado novamente até que seja válido. É necessário que todos os usuários possuam acesso ao sistema para que possam utilizar os serviços prestados pelo hospital, presentes no sistema. 

Ao acessar o sistema, o paciente pode realizar a solicitação de serviços como agendamento e cancelamento de consultas e acompanhar o histórico de consultas (realizadas e agendadas). Também pode gerenciar suas informações de cadastro e ficha médica (medições corporais, enfermidades, observações particulares).

Também devem ser mantidos e cadastrados no sistema, os dados dos médicos que trabalham no hospital. O médico é caracterizado no sistema por um código único, nome completo, CRM, data de nascimento, especialização e email. Para realizar o cadastro de um médico no sistema, é necessário que um administrador do sistema mantenha estes dados. Além disso, o médico também deve ser capaz de manter informações do prontuário médico do paciente e acessar os seus próprios dados no sistema.
