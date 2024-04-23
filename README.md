# Ohjelmistotekniikka, harjoitustyö

#### *Helsingin yliopisto*
Aineopintojen harjoitustyö: **ohjelmistotekniikka, kevät 2024**.

Tulen toteuttamaan tällä kurssilla **pelihahmogeneraattorin**, jonka ideana on arpoa Sims-hahmolle eri piirteet. Piirteillä käyttäjä voi luoda vaivattomasti hahmon Sims-peliin.

Käyttäjä pystyy arpomaan esimerkiksi hahmon hiustyylin sekä -värin ja elämäntavoitteen.

Käyttäjä pystyy myös tallentamaan ja tarkastelemaan luomiansa hahmoja.

## Dokumentaatio
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)

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

