BEGIN;
--
-- Create model Day
--
CREATE TABLE "scheduler_day" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(9) NOT NULL UNIQUE);
--
-- Create model TimeSlot
--
CREATE TABLE "scheduler_timeslot" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "start_time" time NOT NULL, "end_time" time NOT NULL);
--
-- Create model Event
--
CREATE TABLE "scheduler_event" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "description" text NULL, "day_id" bigint NOT NULL REFERENCES "scheduler_day" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "time_slot_id" bigint NOT NULL REFERENCES "scheduler_timeslot" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "scheduler_event_day_id_time_slot_id_user_id_f59a2cb8_uniq" ON "scheduler_event" ("day_id", "time_slot_id", "user_id");
CREATE INDEX "scheduler_event_day_id_fce486b6" ON "scheduler_event" ("day_id");
CREATE INDEX "scheduler_event_user_id_b6c965fa" ON "scheduler_event" ("user_id");
CREATE INDEX "scheduler_event_time_slot_id_6fda67c8" ON "scheduler_event" ("time_slot_id");
COMMIT;
