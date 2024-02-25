--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2
-- Dumped by pg_dump version 16.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: aluminum_etch; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE aluminum_etch (
    id integer NOT NULL,
    chip_number integer NOT NULL,
    chip_owner character varying(64),
    creation_date date,
    alum_etch_temp integer,
    alum_etch_time integer,
    stir_rpm integer,
    metric_alum_etch_depth double precision,
    metric_photoresist_peeling double precision,
    metric_aluminum_peeling double precision,
    metrology_link character varying(512),
    notes character varying(512)
);


--
-- Name: aluminum_evaporation; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE aluminum_evaporation (
    id integer NOT NULL,
    chip_number integer NOT NULL,
    chip_owner character varying(64),
    creation_date date,
    aluminum_evaporation_temp integer[],
    aluminum_evaporation_time integer[],
    pressure_before_start_seq double precision,
    pressure_before_evaporation double precision,
    metric_layer_thickness double precision,
    metric_layer_thick_qcm double precision,
    metric_deposition_rate double precision,
    metrology_link character varying(512),
    notes character varying(512)
);


--
-- Name: chip_list; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE chip_list (
    chip_number integer NOT NULL,
    chip_owner character varying(64),
    creation_date date,
    notes character varying
);


--
-- Name: deposition_template; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE deposition_template (
    id integer NOT NULL,
    chip_number integer NOT NULL,
    chip_owner character varying(64),
    creation_date date,
    cleaning_step character varying(64),
    days_p504_at_room_temp integer,
    prebake_temp integer,
    prebake_time integer,
    amount_drops integer,
    spin_rpm integer,
    spin_time integer,
    bake_temp integer[],
    bake_time integer[],
    humidity integer,
    metric_layer_thickness double precision,
    metric_cracking double precision,
    metric_particles double precision,
    metrology_link character varying(512),
    notes character varying(512)
);


--
-- Name: deposition_700b; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE deposition_700b (
)
INHERITS (deposition_template);


--
-- Name: deposition_p504; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE deposition_p504 (
)
INHERITS (deposition_template);


--
-- Name: oxide_etch; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE oxide_etch (
    id integer NOT NULL,
    chip_number integer NOT NULL,
    chip_owner character varying(64),
    creation_date date,
    max_temp_glass_reached integer,
    oxide_etch_time integer,
    oxide_etch_temp integer,
    metric_oxide_etch_depth double precision,
    metrology_notes character varying(512),
    notes character varying(512)
);


--
-- Name: patterning; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE patterning (
    id integer NOT NULL,
    chip_number integer NOT NULL,
    chip_owner character varying(64),
    creation_date date,
    underlying_material character varying(64),
    hdms_prebake_temp integer,
    hdms_prebake_time integer,
    hdms_spin_rpm integer,
    hdms_spin_time integer,
    hdms_bake_temp integer,
    hdms_bake_time integer,
    photoresist_spin_rpm integer,
    photoresist_spin_time integer,
    photoresist_bake_temp integer,
    photoresist_bake_time integer,
    exposure_pattern character varying(512),
    exposure_time integer,
    develop_time integer,
    metric_pattern_quality double precision,
    metric_leftover_photoresist bit(1),
    metric_missing_photoresist bit(1),
    metric_contaminants double precision,
    metrology_link character varying(512),
    notes character varying(512)
);


--
-- Name: plasma_clean; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE plasma_clean (
    id integer NOT NULL,
    chip_number integer NOT NULL,
    chip_owner character varying(64),
    creation_date date,
    o2_flow double precision,
    rf_power double precision,
    clean_time integer,
    metric_contaminants double precision,
    metrology_notes character varying(512),
    notes character varying(512)
);


--
-- Name: plasma_etch; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE plasma_etch (
    id integer NOT NULL,
    chip_number integer NOT NULL,
    chip_owner character varying(64),
    creation_date date,
    o2_flow double precision,
    sf6_flow double precision,
    rf_power double precision,
    etch_time integer,
    etch_depth double precision,
    notes character varying(256)
);


--
-- Data for Name: aluminum_etch; Type: TABLE DATA; Schema: public; Owner: -
--

COPY aluminum_etch (id, chip_number, chip_owner, creation_date, alum_etch_temp, alum_etch_time, stir_rpm, metric_alum_etch_depth, metric_photoresist_peeling, metric_aluminum_peeling, metrology_link, notes) FROM stdin;
\.


--
-- Data for Name: aluminum_evaporation; Type: TABLE DATA; Schema: public; Owner: -
--

COPY aluminum_evaporation (id, chip_number, chip_owner, creation_date, aluminum_evaporation_temp, aluminum_evaporation_time, pressure_before_start_seq, pressure_before_evaporation, metric_layer_thickness, metric_layer_thick_qcm, metric_deposition_rate, metrology_link, notes) FROM stdin;
\.


--
-- Data for Name: chip_list; Type: TABLE DATA; Schema: public; Owner: -
--

COPY chip_list (chip_number, chip_owner, creation_date, notes) FROM stdin;
\.


--
-- Data for Name: deposition_700b; Type: TABLE DATA; Schema: public; Owner: -
--

COPY deposition_700b (id, chip_number, chip_owner, creation_date, cleaning_step, days_p504_at_room_temp, prebake_temp, prebake_time, amount_drops, spin_rpm, spin_time, bake_temp, bake_time, humidity, metric_layer_thickness, metric_cracking, metric_particles, metrology_link, notes) FROM stdin;
\.


--
-- Data for Name: deposition_p504; Type: TABLE DATA; Schema: public; Owner: -
--

COPY deposition_p504 (id, chip_number, chip_owner, creation_date, cleaning_step, days_p504_at_room_temp, prebake_temp, prebake_time, amount_drops, spin_rpm, spin_time, bake_temp, bake_time, humidity, metric_layer_thickness, metric_cracking, metric_particles, metrology_link, notes) FROM stdin;
\.


--
-- Data for Name: deposition_template; Type: TABLE DATA; Schema: public; Owner: -
--

COPY deposition_template (id, chip_number, chip_owner, creation_date, cleaning_step, days_p504_at_room_temp, prebake_temp, prebake_time, amount_drops, spin_rpm, spin_time, bake_temp, bake_time, humidity, metric_layer_thickness, metric_cracking, metric_particles, metrology_link, notes) FROM stdin;
\.


--
-- Data for Name: oxide_etch; Type: TABLE DATA; Schema: public; Owner: -
--

COPY oxide_etch (id, chip_number, chip_owner, creation_date, max_temp_glass_reached, oxide_etch_time, oxide_etch_temp, metric_oxide_etch_depth, metrology_notes, notes) FROM stdin;
\.


--
-- Data for Name: patterning; Type: TABLE DATA; Schema: public; Owner: -
--

COPY patterning (id, chip_number, chip_owner, creation_date, underlying_material, hdms_prebake_temp, hdms_prebake_time, hdms_spin_rpm, hdms_spin_time, hdms_bake_temp, hdms_bake_time, photoresist_spin_rpm, photoresist_spin_time, photoresist_bake_temp, photoresist_bake_time, exposure_pattern, exposure_time, develop_time, metric_pattern_quality, metric_leftover_photoresist, metric_missing_photoresist, metric_contaminants, metrology_link, notes) FROM stdin;
\.


--
-- Data for Name: plasma_clean; Type: TABLE DATA; Schema: public; Owner: -
--

COPY plasma_clean (id, chip_number, chip_owner, creation_date, o2_flow, rf_power, clean_time, metric_contaminants, metrology_notes, notes) FROM stdin;
\.


--
-- Data for Name: plasma_etch; Type: TABLE DATA; Schema: public; Owner: -
--

COPY plasma_etch (id, chip_number, chip_owner, creation_date, o2_flow, sf6_flow, rf_power, etch_time, etch_depth, notes) FROM stdin;
\.


--
-- Name: aluminum_etch aluminum_etch_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY aluminum_etch
    ADD CONSTRAINT aluminum_etch_pkey PRIMARY KEY (id);


--
-- Name: aluminum_evaporation aluminum_evaporation_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY aluminum_evaporation
    ADD CONSTRAINT aluminum_evaporation_pkey PRIMARY KEY (id);


--
-- Name: chip_list chip_number; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY chip_list
    ADD CONSTRAINT chip_number PRIMARY KEY (chip_number);


--
-- Name: deposition_700b deposition_700b_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY deposition_700b
    ADD CONSTRAINT deposition_700b_pkey PRIMARY KEY (id);


--
-- Name: deposition_p504 deposition_p504_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY deposition_p504
    ADD CONSTRAINT deposition_p504_pkey PRIMARY KEY (id);


--
-- Name: oxide_etch oxide_etch_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY oxide_etch
    ADD CONSTRAINT oxide_etch_pkey PRIMARY KEY (id);


--
-- Name: deposition_template p504_deposition_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY deposition_template
    ADD CONSTRAINT p504_deposition_pkey PRIMARY KEY (id);


--
-- Name: patterning patterning_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY patterning
    ADD CONSTRAINT patterning_pkey PRIMARY KEY (id);


--
-- Name: plasma_clean plasma_clean_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY plasma_clean
    ADD CONSTRAINT plasma_clean_pkey PRIMARY KEY (id);


--
-- Name: plasma_etch plasma_etch_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY plasma_etch
    ADD CONSTRAINT plasma_etch_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

