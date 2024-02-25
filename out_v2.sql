CREATE TABLE aluminum_etch (
    id integer PRIMARY KEY NOT NULL,
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
    id integer PRIMARY KEY NOT NULL,
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
    chip_number integer PRIMARY KEY NOT NULL,
    chip_owner character varying(64),
    creation_date date,
    notes character varying
);


--
-- Name: deposition_template; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE deposition_template (
    id integer PRIMARY KEY NOT NULL,
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
    id integer PRIMARY KEY NOT NULL,
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
    id integer PRIMARY KEY NOT NULL,
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
    id integer PRIMARY KEY NOT NULL,
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
    id integer PRIMARY KEY NOT NULL,
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

