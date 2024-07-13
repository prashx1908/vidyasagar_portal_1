PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO django_migrations VALUES(1,'contenttypes','0001_initial','2024-07-12 17:34:52.154788');
INSERT INTO django_migrations VALUES(2,'contenttypes','0002_remove_content_type_name','2024-07-12 17:34:52.158536');
INSERT INTO django_migrations VALUES(3,'auth','0001_initial','2024-07-12 17:34:52.165504');
INSERT INTO django_migrations VALUES(4,'auth','0002_alter_permission_name_max_length','2024-07-12 17:34:52.169023');
INSERT INTO django_migrations VALUES(5,'auth','0003_alter_user_email_max_length','2024-07-12 17:34:52.171363');
INSERT INTO django_migrations VALUES(6,'auth','0004_alter_user_username_opts','2024-07-12 17:34:52.173897');
INSERT INTO django_migrations VALUES(7,'auth','0005_alter_user_last_login_null','2024-07-12 17:34:52.176591');
INSERT INTO django_migrations VALUES(8,'auth','0006_require_contenttypes_0002','2024-07-12 17:34:52.177648');
INSERT INTO django_migrations VALUES(9,'auth','0007_alter_validators_add_error_messages','2024-07-12 17:34:52.181502');
INSERT INTO django_migrations VALUES(10,'auth','0008_alter_user_username_max_length','2024-07-12 17:34:52.184620');
INSERT INTO django_migrations VALUES(11,'auth','0009_alter_user_last_name_max_length','2024-07-12 17:34:52.187281');
INSERT INTO django_migrations VALUES(12,'auth','0010_alter_group_name_max_length','2024-07-12 17:34:52.190592');
INSERT INTO django_migrations VALUES(13,'auth','0011_update_proxy_permissions','2024-07-12 17:34:52.192962');
INSERT INTO django_migrations VALUES(14,'auth','0012_alter_user_first_name_max_length','2024-07-12 17:34:52.195414');
INSERT INTO django_migrations VALUES(15,'app','0001_initial','2024-07-12 17:34:52.201500');
INSERT INTO django_migrations VALUES(16,'admin','0001_initial','2024-07-12 17:34:52.206292');
INSERT INTO django_migrations VALUES(17,'admin','0002_logentry_remove_auto_add','2024-07-12 17:34:52.212154');
INSERT INTO django_migrations VALUES(18,'admin','0003_logentry_add_action_flag_choices','2024-07-12 17:34:52.215663');
INSERT INTO django_migrations VALUES(19,'app','0002_course','2024-07-12 17:34:52.217293');
INSERT INTO django_migrations VALUES(20,'app','0003_student','2024-07-12 17:34:52.222167');
INSERT INTO django_migrations VALUES(21,'app','0004_customuser_student_details_link_and_more','2024-07-12 17:34:52.231560');
INSERT INTO django_migrations VALUES(22,'app','0005_staff','2024-07-12 17:34:52.237217');
INSERT INTO django_migrations VALUES(23,'app','0006_delete_staff','2024-07-12 17:34:52.238410');
INSERT INTO django_migrations VALUES(24,'app','0007_staff','2024-07-12 17:34:52.244345');
INSERT INTO django_migrations VALUES(25,'app','0008_alter_staff_department','2024-07-12 17:34:52.249680');
INSERT INTO django_migrations VALUES(26,'app','0009_customuser_department_alter_customuser_user_type','2024-07-12 17:34:52.258010');
INSERT INTO django_migrations VALUES(27,'app','0010_timetable','2024-07-12 17:34:52.263701');
INSERT INTO django_migrations VALUES(28,'app','0011_delete_timetable','2024-07-12 17:34:52.264983');
INSERT INTO django_migrations VALUES(29,'app','0012_timetable','2024-07-12 17:34:52.270395');
INSERT INTO django_migrations VALUES(30,'app','0013_delete_timetable','2024-07-12 17:34:52.271522');
INSERT INTO django_migrations VALUES(31,'app','0014_alter_customuser_user_type','2024-07-12 17:34:52.277246');
INSERT INTO django_migrations VALUES(32,'sessions','0001_initial','2024-07-12 17:34:52.279300');
CREATE TABLE IF NOT EXISTS "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
INSERT INTO django_content_type VALUES(1,'admin','logentry');
INSERT INTO django_content_type VALUES(2,'auth','permission');
INSERT INTO django_content_type VALUES(3,'auth','group');
INSERT INTO django_content_type VALUES(4,'contenttypes','contenttype');
INSERT INTO django_content_type VALUES(5,'sessions','session');
INSERT INTO django_content_type VALUES(6,'app','customuser');
INSERT INTO django_content_type VALUES(7,'app','course');
INSERT INTO django_content_type VALUES(8,'app','student');
INSERT INTO django_content_type VALUES(9,'app','staff');
CREATE TABLE IF NOT EXISTS "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
INSERT INTO auth_permission VALUES(1,1,'add_logentry','Can add log entry');
INSERT INTO auth_permission VALUES(2,1,'change_logentry','Can change log entry');
INSERT INTO auth_permission VALUES(3,1,'delete_logentry','Can delete log entry');
INSERT INTO auth_permission VALUES(4,1,'view_logentry','Can view log entry');
INSERT INTO auth_permission VALUES(5,2,'add_permission','Can add permission');
INSERT INTO auth_permission VALUES(6,2,'change_permission','Can change permission');
INSERT INTO auth_permission VALUES(7,2,'delete_permission','Can delete permission');
INSERT INTO auth_permission VALUES(8,2,'view_permission','Can view permission');
INSERT INTO auth_permission VALUES(9,3,'add_group','Can add group');
INSERT INTO auth_permission VALUES(10,3,'change_group','Can change group');
INSERT INTO auth_permission VALUES(11,3,'delete_group','Can delete group');
INSERT INTO auth_permission VALUES(12,3,'view_group','Can view group');
INSERT INTO auth_permission VALUES(13,4,'add_contenttype','Can add content type');
INSERT INTO auth_permission VALUES(14,4,'change_contenttype','Can change content type');
INSERT INTO auth_permission VALUES(15,4,'delete_contenttype','Can delete content type');
INSERT INTO auth_permission VALUES(16,4,'view_contenttype','Can view content type');
INSERT INTO auth_permission VALUES(17,5,'add_session','Can add session');
INSERT INTO auth_permission VALUES(18,5,'change_session','Can change session');
INSERT INTO auth_permission VALUES(19,5,'delete_session','Can delete session');
INSERT INTO auth_permission VALUES(20,5,'view_session','Can view session');
INSERT INTO auth_permission VALUES(21,6,'add_customuser','Can add user');
INSERT INTO auth_permission VALUES(22,6,'change_customuser','Can change user');
INSERT INTO auth_permission VALUES(23,6,'delete_customuser','Can delete user');
INSERT INTO auth_permission VALUES(24,6,'view_customuser','Can view user');
INSERT INTO auth_permission VALUES(25,7,'add_course','Can add course');
INSERT INTO auth_permission VALUES(26,7,'change_course','Can change course');
INSERT INTO auth_permission VALUES(27,7,'delete_course','Can delete course');
INSERT INTO auth_permission VALUES(28,7,'view_course','Can view course');
INSERT INTO auth_permission VALUES(29,8,'add_student','Can add student');
INSERT INTO auth_permission VALUES(30,8,'change_student','Can change student');
INSERT INTO auth_permission VALUES(31,8,'delete_student','Can delete student');
INSERT INTO auth_permission VALUES(32,8,'view_student','Can view student');
INSERT INTO auth_permission VALUES(33,9,'add_staff','Can add staff');
INSERT INTO auth_permission VALUES(34,9,'change_staff','Can change staff');
INSERT INTO auth_permission VALUES(35,9,'delete_staff','Can delete staff');
INSERT INTO auth_permission VALUES(36,9,'view_staff','Can view staff');
CREATE TABLE IF NOT EXISTS "auth_group" (
    "id" SERIAL PRIMARY KEY,
    "name" varchar(150) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS "app_customuser_groups" (
    "id" SERIAL PRIMARY KEY,
    "customuser_id" bigint NOT NULL REFERENCES "app_customuser" ("id") DEFERRABLE INITIALLY DEFERRED,
    "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS "app_customuser_user_permissions" (
    "id" SERIAL PRIMARY KEY,
    "customuser_id" bigint NOT NULL REFERENCES "app_customuser" ("id") DEFERRABLE INITIALLY DEFERRED,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS "django_admin_log" (
    "id" SERIAL PRIMARY KEY,
    "object_id" text NULL,
    "object_repr" varchar(200) NOT NULL,
    "action_flag" smallint NOT NULL CHECK ("action_flag" >= 0),
    "change_message" text NOT NULL,
    "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED,
    "user_id" bigint NOT NULL REFERENCES "app_customuser" ("id") DEFERRABLE INITIALLY DEFERRED,
    "action_time" timestamp NOT NULL
);

CREATE TABLE IF NOT EXISTS "app_course" (
    "id" SERIAL PRIMARY KEY,
    "name" varchar(100) NOT NULL,
    "created_at" timestamp NOT NULL,
    "updated_at" timestamp NOT NULL
);

CREATE TABLE IF NOT EXISTS "app_student" (
    "id" SERIAL PRIMARY KEY,
    "address" text NOT NULL,
    "gender" varchar(100) NOT NULL,
    "created_at" timestamp NOT NULL,
    "updated_at" timestamp NOT NULL,
    "admin_id" bigint NOT NULL UNIQUE REFERENCES "app_customuser" ("id") DEFERRABLE INITIALLY DEFERRED,
    "course_id" bigint NOT NULL REFERENCES "app_course" ("id") DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE IF NOT EXISTS "app_staff" (
    "id" SERIAL PRIMARY KEY,
    "address" text NOT NULL,
    "gender" varchar(100) NOT NULL,
    "created_at" timestamp NOT NULL,
    "updated_at" timestamp NOT NULL,
    "admin_id" bigint NOT NULL UNIQUE REFERENCES "app_customuser" ("id") DEFERRABLE INITIALLY DEFERRED,
    "department" varchar(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS "app_customuser" (
    "id" SERIAL PRIMARY KEY,
    "password" varchar(128) NOT NULL,
    "last_login" timestamp NULL,
    "is_superuser" bool NOT NULL,
    "username" varchar(150) NOT NULL UNIQUE,
    "first_name" varchar(150) NOT NULL,
    "last_name" varchar(150) NOT NULL,
    "email" varchar(254) NOT NULL,
    "is_staff" bool NOT NULL,
    "is_active" bool NOT NULL,
    "date_joined" timestamp NOT NULL,
    "profile_pic" varchar(100) NULL,
    "student_details_link" varchar(200) NULL,
    "department" varchar(100) NULL,
    "user_type" varchar(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS "django_session" (
    "session_key" varchar(40) NOT NULL PRIMARY KEY,
    "session_data" text NOT NULL,
    "expire_date" timestamp NOT NULL
);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('django_migrations',32);
INSERT INTO sqlite_sequence VALUES('django_content_type',9);
INSERT INTO sqlite_sequence VALUES('auth_permission',36);
INSERT INTO sqlite_sequence VALUES('auth_group',0);
INSERT INTO sqlite_sequence VALUES('django_admin_log',0);
INSERT INTO sqlite_sequence VALUES('app_staff',0);
INSERT INTO sqlite_sequence VALUES('app_customuser',0);
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE UNIQUE INDEX "app_customuser_groups_customuser_id_group_id_a5a0ca22_uniq" ON "app_customuser_groups" ("customuser_id", "group_id");
CREATE INDEX "app_customuser_groups_customuser_id_164d073f" ON "app_customuser_groups" ("customuser_id");
CREATE INDEX "app_customuser_groups_group_id_47e49ebd" ON "app_customuser_groups" ("group_id");
CREATE UNIQUE INDEX "app_customuser_user_permissions_customuser_id_permission_id_22e31019_uniq" ON "app_customuser_user_permissions" ("customuser_id", "permission_id");
CREATE INDEX "app_customuser_user_permissions_customuser_id_4bcbaafb" ON "app_customuser_user_permissions" ("customuser_id");
CREATE INDEX "app_customuser_user_permissions_permission_id_c5920c75" ON "app_customuser_user_permissions" ("permission_id");
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE INDEX "app_student_course_id_id_f104d091" ON "app_student" ("course_id_id");
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
COMMIT;
