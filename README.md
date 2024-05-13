# TS4-pelihahmogeneraattori

Aineopintojen harjoitustyö: **ohjelmistotekniikka, kevät 2024**.

Tulen toteuttamaan tällä kurssilla **pelihahmogeneraattorin**, jonka ideana on arpoa Sims-hahmolle eri piirteet. Piirteillä käyttäjä voi luoda vaivattomasti hahmon The Sims 4-peliin.

Käyttäjä pystyy arpomaan esimerkiksi hahmon hiustyylin sekä -värin ja elämäntavoitteen.

Käyttäjä pystyy myös tallentamaan ja tarkastelemaan luomiansa hahmoja.

## Dokumentaatio
- [Käyttöohje](./dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)

## Release
- [Viikko 5](https://github.com/mkekola/ot-harjoitustyo/releases/tag/viikko5)
- [Viikko 6](https://github.com/mkekola/ot-harjoitustyo/releases/tag/viikko6)

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

