PGDMP         8    
        
    {         	   django_db    11.21    11.21     �
           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false                        0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false                       1262    32970 	   django_db    DATABASE     �   CREATE DATABASE django_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Russian_Russia.1252' LC_CTYPE = 'Russian_Russia.1252';
    DROP DATABASE django_db;
             postgres    false                        2615    32971 	   my_schema    SCHEMA        CREATE SCHEMA my_schema;
    DROP SCHEMA my_schema;
             postgres    false            �            1259    32974    users    TABLE     �   CREATE TABLE my_schema.users (
    id bigint NOT NULL,
    login character varying NOT NULL,
    password character varying NOT NULL
);
    DROP TABLE my_schema.users;
    	   my_schema         postgres    false    6            �            1259    32972    users_id_seq    SEQUENCE     x   CREATE SEQUENCE my_schema.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE my_schema.users_id_seq;
    	   my_schema       postgres    false    6    198                       0    0    users_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE my_schema.users_id_seq OWNED BY my_schema.users.id;
         	   my_schema       postgres    false    197            
           2604    32977    users id    DEFAULT     j   ALTER TABLE ONLY my_schema.users ALTER COLUMN id SET DEFAULT nextval('my_schema.users_id_seq'::regclass);
 :   ALTER TABLE my_schema.users ALTER COLUMN id DROP DEFAULT;
    	   my_schema       postgres    false    198    197    198            �
          0    32974    users 
   TABLE DATA               7   COPY my_schema.users (id, login, password) FROM stdin;
 	   my_schema       postgres    false    198                      0    0    users_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('my_schema.users_id_seq', 1, false);
         	   my_schema       postgres    false    197            �
           2606    32982    users users_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY my_schema.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 =   ALTER TABLE ONLY my_schema.users DROP CONSTRAINT users_pkey;
    	   my_schema         postgres    false    198            �
      x������ � �     