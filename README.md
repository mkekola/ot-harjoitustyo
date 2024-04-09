# Ohjelmistotekniikka, harjoitustyö

#### *Helsingin yliopisto*
Aineopintojen harjoitustyö: **ohjelmistotekniikka, kevät 2024**.

Tulen toteuttamaan tällä kurssilla **pelihahmo generaattorin**.

## Dokumentaatio
- [Laskarit](https://github.com/mkekola/ot-harjoitustyo/tree/master/laskarit)
- [Vaatimusmäärittely](https://github.com/mkekola/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](https://github.com/mkekola/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/mkekola/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

## Asennus

```bash
poetry init --python "^3.8"
```

```bash
poetry install
```

```bash
poetry add invoke
```

## Komennot

### Ohjelman suoritus

```bash
poetry run invoke start
```

### Testien suoritus

```bash
poetry run invoke test
```

### Testien kattavuus html

```bash
poetry run invoke coverage-report
```

### Pylint tarkastus

```bash
poetry run invoke lint
```

