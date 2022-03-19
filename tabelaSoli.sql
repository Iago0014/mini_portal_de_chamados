create database if not exists db_manutencao;

use db_manutencao;

create table solicitante(idSolicitente integer primary key auto_increment, 
localidade varchar(45), nome varchar(45), dataSolicitacao datetime, dataFecha datetime, setor varchar(65), 
comentario varchar(255), status boolean);

alter table solicitante modify column dataSolicitacao datetime;

alter table solicitante add column status boolean;

alter table solicitante add column dataFecha datetime;

select * from solicitante order by idSolicitente desc;

desc solicitante;

create table usuarios (idusuario integer primary key auto_increment, nomeUser varchar(45), senhaUser varchar(15));
desc usuarios;

insert into usuarios(nomeUser, senhaUser) values ('Iago', 'senha123');

select * from usuarios;

update solicitante set status = false, dataFecha = '2022-02-12 21:25:00' where idSolicitente = 12;

update solicitante set dataFecha = '12-02-2022 21:25:00' where idSolicitente = 12;
(STR_TO_DATE(LoginDate,'%d.%m.%Y'), '%Y-%m-%d') as DateFormat from
select idSolicitente, localidade, nome, dataSolicitacao, setor, comentario, status, DATE_FORMAT(dataFecha,'%d.%m.%Y %H:%i:%S') as dataFecha from solicitante;

alter table usuarios add column emailUser varchar(65);

update usuarios set emailUser = 'iago@gmail.com' where idusuario = 1;