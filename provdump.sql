PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "homedata_exchanges" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "DATE" datetime NOT NULL, "EXCH" varchar(10) NOT NULL, "EXCH_FULL" varchar(100) NOT NULL);
INSERT INTO "homedata_exchanges" VALUES(1,'2017-02-10 05:55:56','MSE','Malta Stock Exchange');
COMMIT;
