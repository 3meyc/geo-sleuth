# Ukraine clues

Entries use the shared format (`references/clues/README.md`). Clues that tell Ukraine apart from other countries belong in `references/clues/global.md`. Sources were checked on 2026-10-28; codes follow the official assignment to oblasts.

## Text and numbers

### Region code at the start of a civil number plate
- Look for: the two letters on the left of a white plate with the blue-and-yellow flag and `UA` in a blue band: `ВН 1234 АХ`. Only the 12 Cyrillic letters that look Latin are used (А В Е І К М Н О Р С Т Х), so OCR often returns Latin; both work
- Points to: the oblast where the vehicle was **registered** → `clues.py lookup plate <plate> --country ua` or `board.py apply --kind plate --value <plate>`. Each oblast has four codes (2004, 2013 and two from 2021): Odesa ВН/НН/ОО/ЕН; the city of Kyiv АА/КА/ТТ/КК and the Kyiv oblast around it АІ/КІ/ТІ/ЕЕ are separate. A 2013 or 2021 code also dates the registration to after that year
- Strength: weak for where the photo was taken; medium when most parked cars in a quiet residential street share one oblast
- Counterexamples: since December 2022 cars registered online carry `ED`/`DC` (driver's e-cabinet) or `DI`/`PD` (Diia) instead of a region; fleet and leased cars are often registered in Kyiv; refugees and relocated businesses since 2022 drive far from their home oblast; Bulgarian plates use the same letter set and layout (`СВ 1234 АВ` is Sofia) but carry the EU band with `BG`; personalised plates have free text
- Sources: MVS order 166 of 02.03.2021, Annex 4 (codes) and section VIII.5 (online codes), https://zakon.rada.gov.ua/laws/show/z0353-21; uk.wikipedia "Номерні знаки України" (code eras, ІІ series), https://uk.wikipedia.org/wiki/Номерні_знаки_України

### Numeric region code on a 1995–2004 plate
- Look for: an older white plate with five digits split by a dash and two letters (`123-45 ОА`), and a small two-digit number under the flag on the left
- Points to: the oblast of registration, numbered 01–27 (16 Odesa, 10 Kyiv oblast, 11 the city of Kyiv, 27 Sevastopol) → `clues.py lookup plate "16 123-45 ОА" --country ua` (type the small number first)
- Strength: weak (single source); these plates are still valid but now rare, mostly on old cars in villages and small towns
- Counterexamples: 28 was a nationwide series; a car bought second-hand keeps its old plate after moving to another oblast; the small number is easy to misread from a distance
- Sources: uk.wikipedia "Номерні знаки України", section 1995—2004 (code table), https://uk.wikipedia.org/wiki/Номерні_знаки_України; en.wikipedia "Vehicle registration plates of Ukraine" (format, 27 = Sevastopol), https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Ukraine

### Landline zone code on shop signs and vehicles
- Look for: a fixed-line number on a sign, awning, van or banner: `(048) 7xx-xx-xx`, `044 …`, or an old town code such as `(04849) 2-34-56`
- Points to: the oblast of that landline → `clues.py lookup area-code <number> --country ua`. One code per oblast; 044 is the city of Kyiv only and 045 the Kyiv oblast around it; 069 is Sevastopol and 065 Crimea. Longer town codes start with the oblast code, so they resolve to the oblast; town-level codes are not in the table
- Strength: medium (official numbering plan; a shop's own landline is usually local)
- Counterexamples: mobile numbers (050, 063, 066, 067, 068, 073, 093, 095–099 and others) are not geographic and are far more common on signs than landlines; 0800 and short numbers are nationwide; a chain's sign can show its head-office number; numbers written as `+38 (0xx)` must be read without the `+38`
- Sources: National Numbering Plan of Ukraine, order 758 of 26.08.2023, Annex 1 (zone and mobile codes), https://zakon.rada.gov.ua/laws/show/z1534-23

### Territorial road number → oblast
- Look for: a route marker or kilometre post with `Т-16-07`, or a blue route shield `Т-xx-xx` on a direction sign
- Points to: the two digits after Т are the oblast index, in the same 01–27 order as 1995–2004 plates → `clues.py lookup road-number Т-16-07 --country ua`; then `osm.py route` on that road
- Strength: medium (official road list; Wikipedia groups it by oblast)
- Counterexamples: a few roads keep their index across an oblast border (Т-04 roads in Zaporizhzhia and Kherson oblasts, Т-17 roads in Sumy oblast); a sign at a junction can name a road that starts in the next oblast; `М`, `Н` and `Р` numbers are nationwide and carry no oblast index
- Sources: Cabinet resolution 1318 of 15.12.2023 (list of state roads), https://zakon.rada.gov.ua/laws/show/1318-2023-п; uk.wikipedia "Територіальні автомобільні шляхи України", https://uk.wikipedia.org/wiki/Територіальні_автомобільні_шляхи_України

### Route shield colours on direction signs
- Look for: the coloured box with a road number on a direction sign
- Points to: road class: `Є` (E-road) white on green; `М` (international) and `Н` (national) white on red; `Р` (regional) and `Т` (territorial) white on blue; `О` (oblast) and `С` (raion) black on white. A red shield means a main corridor; `Т` leads to the oblast lookup above
- Strength: medium (single source: the traffic rules)
- Counterexamples: old signs survive with outdated numbers after the 2023 renumbering of state roads; a shield names the road the sign points to, not always the road the camera stands on
- Sources: Traffic Rules of Ukraine, Cabinet resolution 1306 of 10.10.2001, signs 5.59–5.60, https://zakon.rada.gov.ua/laws/show/1306-2001-п

## Language and script

### Ukrainian letters on signs, and Russian-only letters
- Look for: і, ї, є, ґ and the apostrophe in words (Ukrainian); ы, э, ъ, ё (Russian only)
- Points to: municipal and official signs, street names and shop signs in Ukraine are in Ukrainian by law (state-language law 2704-VIII: public information art. 28, customer service art. 30, street and place names art. 41). A Russian-only shop sign in Ukraine points to an older photo or an informal sign; `ґ` on an official sign dates it after 1990, when the letter was restored to the orthography
- Strength: weak for the region within Ukraine; Russian-language signage was common in the south and east before the law, which is a soft hint only
- Counterexamples: Belarusian also uses і (but not ї, є, ґ); brand names, menus and private notices stay in Russian or English; areas under occupation since 2014 or 2022 have Russian signage; a photo from before 2019 can show Russian signs anywhere
- Sources: law of Ukraine 2704-VIII of 25.04.2019, arts. 28, 30, 41, https://zakon.rada.gov.ua/laws/show/2704-19; uk.wikipedia "Українська абетка" (33 letters; ґ removed in 1933, restored in 1990), https://uk.wikipedia.org/wiki/Українська_абетка

## Street furniture

### Kyiv address plates: dark-blue enamel, name and number apart
- Look for: a horizontal dark-blue enamel plate on a facade, white lettering, the street name and the house number in separate fields
- Points to: Kyiv (city-wide standard designed by Agenty Zmin and approved by the city administration in 2019)
- Strength: medium (two sources)
- Counterexamples: old Soviet-era dark-blue plates and private lightboxes still hang next to the new ones; other cities copied similar designs; renamed streets get new plates first, so an old plate can carry a former name
- Sources: Glavcom 08.11.2016, "Дизайн адресних табличок у Києві планують змінити", https://glavcom.ua/kyiv/news/dizayn-adresnih-tablichok-u-kijevi-planuyut-zminiti-381724.html; uk.wikipedia "Вуличний покажчик" (2019 standard), https://uk.wikipedia.org/wiki/Вуличний_покажчик

### Lviv street plates with Latin transliteration
- Look for: enamel street plates with the Ukrainian name and a smaller Latin transliteration below it, left-aligned, in a period-style typeface (Municipal); in newer districts square blue plates combine the name and the house number
- Points to: Lviv (system installed from 2010); Ternopil uses an identical design
- Strength: medium (single source, with its own references)
- Counterexamples: many cities added transliterated plates later with their own designs; by 2022 a large part of Lviv's tourist signage was lost, so absence says little
- Sources: uk.wikipedia "Вуличний покажчик", section Львів, https://uk.wikipedia.org/wiki/Вуличний_покажчик

### Public-transport stop signs, and the Kyiv no-smoking plate
- Look for: the blue square stop sign (bus 5.45.1, tram 5.46.1, trolleybus 5.47.1) on a pole; in Kyiv a white panel below it with route numbers and a bilingual plate «ЗАБОРОНЕНО (NO SMOKING)»
- Points to: the sign itself only says Ukraine-style stop; the white route panel with the bilingual Ukrainian/English no-smoking plate matched the Kyiv standard in a real case
- Strength: medium (single source: case)
- Counterexamples: smoking at stops is banned nationwide and a graphic no-smoking notice is required everywhere, so a no-smoking plate alone is not Kyiv; Lviv used brown route tables with a yellow top (2012); stop furniture is replaced often, check the capture date
- Sources: case (Kyiv tram stop); Traffic Rules of Ukraine, signs 5.45–5.47, https://zakon.rada.gov.ua/laws/show/1306-2001-п; tobacco law 2899-IV art. 13 (ban at stops, required notice), https://zakon.rada.gov.ua/laws/show/2899-15; uk.wikipedia "Вуличний покажчик" (Lviv route tables), https://uk.wikipedia.org/wiki/Вуличний_покажчик

## Transport

### Tram tracks or a single overhead wire
- Look for: rails in the street, or one overhead contact wire (a tram's pantograph) rather than the two parallel wires of a trolleybus line
- Points to: one of the 17 cities with a tram system: Kyiv, Odesa, Lviv, Kharkiv, Dnipro, Zaporizhzhia, Mykolaiv, Vinnytsia, Zhytomyr, Kryvyi Rih, Kamianske, Konotop, Donetsk, Horlivka, Yenakiieve, Yevpatoria, and Mariupol (stopped in 2022). Lviv, Vinnytsia, Zhytomyr and Yevpatoria run metre gauge, the others 1524 mm
- Strength: medium (single source; it rules out every other town)
- Counterexamples: tracks left after a system closed (Kropyvnytskyi, Chernivtsi, Kremenchuk, Sevastopol, Simferopol, Luhansk, Kramatorsk and others); industrial and port railways in streets; two wires mean a trolleybus, which runs in many more cities
- Sources: uk.wikipedia "Список трамвайних систем України" (list, map of working systems with gauge), https://uk.wikipedia.org/wiki/Список_трамвайних_систем_України

## Buildings

### Kyiv large-panel series 96 and 134
- Look for: 9- to 16-storey panel blocks from 1975 to the 1990s, often in long sections or curved plans; series 134 has rectangular attic windows, series 96 square ones
- Points to: Kyiv's residential districts of the 1970s–80s (Obolon, Troieshchyna, Zaliznychnyi masyv, Berkovets); both series were designed for building in Kyiv
- Strength: weak (single source per series)
- Counterexamples: series 96 was also built in Odesa, Ivano-Frankivsk, Zaporizhzhia, Khmelnytskyi, Luhansk and in Russia; 134 in Donetsk and Volgograd; facade insulation hides the panels
- Sources: uk.wikipedia "111-96", https://uk.wikipedia.org/wiki/111-96; uk.wikipedia "111-134", https://uk.wikipedia.org/wiki/111-134

### 1-КГ-480 «чешка» five- and nine-storey blocks
- Look for: 5- or 9-storey blocks of expanded-clay concrete panels from the 1960s–70s, some with balconies in a chequerboard pattern (1968–1975)
- Points to: Kyiv (a series designed for Kyiv as a deeper variant of 1-480)
- Strength: weak (single source)
- Counterexamples: the much more widespread 1-480 and 1-464 khrushchyovkas look alike from a distance; chequerboard balconies also occur in other series
- Sources: uk.wikipedia "1-КГ-480", https://uk.wikipedia.org/wiki/1-КГ-480

### Shell-limestone walls
- Look for: walls of porous yellowish-grey blocks of shell limestone (черепашник), bare or under peeling plaster, on low houses, fences and old courtyards
- Points to: Odesa and the Black Sea steppe around it, where the stone was quarried (the Odesa catacombs are its old quarries)
- Strength: weak (single source)
- Counterexamples: the same stone is used along the whole northern Black Sea coast, in Mykolaiv, Kherson and Crimea; plastered walls hide it
- Sources: uk.wikipedia "Одеса" (building material), https://uk.wikipedia.org/wiki/Одеса; uk.wikipedia "Одеські катакомби", https://uk.wikipedia.org/wiki/Одеські_катакомби

## Roads

### Direction-sign background colour
- Look for: the background of direction and advance-direction signs (5.57–5.60)
- Points to: green = on a motorway; blue = on another road outside a settlement; white = inside a settlement; brown = a tourist attraction. A coloured inset shows which kind of road leads to that destination
- Strength: medium (single source: the traffic rules)
- Counterexamples: worn or temporary signs; neighbouring countries use similar Vienna-convention colours, so it says nothing about the country
- Sources: Traffic Rules of Ukraine, signs 5.57–5.60, https://zakon.rada.gov.ua/laws/show/1306-2001-п

## Gaps (not clues)

Not in the pack yet, checked on 2026-10-28: town-level landline codes (no official list; the Wikipedia list "Список телефонних кодів України" has no inline citations); mobile operator per code (not geographic); Odesa and Kharkiv street-plate and stop designs (no source found); a trolleybus city list; postal codes.
