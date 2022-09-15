CREATE TABLE `goods` (
	`IdTovar` INT(11) NOT NULL AUTO_INCREMENT COMMENT 'Код товара',
	`Artikul` VARCHAR(255) NULL DEFAULT NULL COMMENT 'Артикул товар' COLLATE 'utf8mb4_unicode_ci',
	`Name` VARCHAR(255) NULL DEFAULT NULL COMMENT 'Название товара' COLLATE 'utf8mb4_unicode_ci',
	`Edizm` VARCHAR(10) NULL DEFAULT 'Рубли' COMMENT 'Единица измерения' COLLATE 'utf8mb4_unicode_ci',
	`Zena` FLOAT NULL DEFAULT NULL COMMENT 'Цена за единицу измерения',
	PRIMARY KEY (`IdTovar`) USING BTREE
)
COMMENT='Товары'
COLLATE='utf8mb4_unicode_ci'
ENGINE=InnoDB
;


CREATE TABLE `suppliers` (
	`IdPostav` INT(11) NOT NULL AUTO_INCREMENT COMMENT 'Код поставщика',
	`Postav` VARCHAR(50) NOT NULL DEFAULT '' COMMENT 'Наименование поставщика' COLLATE 'utf8mb4_unicode_ci',
	`Gorod` VARCHAR(20) NULL DEFAULT '' COMMENT 'Код города ' COLLATE 'utf8mb4_unicode_ci',
	`Ulica` VARCHAR(20) NULL DEFAULT '' COMMENT 'Код улицы' COLLATE 'utf8mb4_unicode_ci',
	`Dom` VARCHAR(20) NULL DEFAULT '' COMMENT 'Дом' COLLATE 'utf8mb4_unicode_ci',
	`Korpus` VARCHAR(20) NULL DEFAULT '' COMMENT 'Корпус' COLLATE 'utf8mb4_unicode_ci',
	`Kv` VARCHAR(20) NULL DEFAULT '' COMMENT 'Квартира' COLLATE 'utf8mb4_unicode_ci',
	`Telef` INT(15) NULL DEFAULT NULL COMMENT 'Телефон',
	PRIMARY KEY (`IdPostav`) USING BTREE
)
COMMENT='Поставщики'
COLLATE='utf8mb4_unicode_ci'
ENGINE=InnoDB
;


CREATE TABLE `receipts` (
	`IdPrihod` INT(11) NOT NULL AUTO_INCREMENT COMMENT 'Код поступления',
	`IdTovar` INT(11) NULL DEFAULT NULL COMMENT 'Код товара',
	`IdPostav` INT(11) NULL DEFAULT NULL COMMENT 'Код поставщика ',
	`DatPrih` DATE NULL DEFAULT NULL COMMENT 'Дата прихода',
	`Kolvo` INT(4) NULL DEFAULT NULL COMMENT 'Количество',
	PRIMARY KEY (`IdPrihod`) USING BTREE,
	INDEX `FK__goods` (`IdTovar`) USING BTREE,
	INDEX `FK_receipts_suppliers` (`IdPostav`) USING BTREE,
	CONSTRAINT `FK__goods` FOREIGN KEY (`IdTovar`) REFERENCES `goods` (`IdTovar`) ON UPDATE NO ACTION ON DELETE NO ACTION,
	CONSTRAINT `FK_receipts_suppliers` FOREIGN KEY (`IdPostav`) REFERENCES `suppliers` (`IdPostav`) ON UPDATE NO ACTION ON DELETE NO ACTION
)
COMMENT='Поступления товаров'
COLLATE='utf8mb4_unicode_ci'
ENGINE=InnoDB
;
