# Dungeon-Crawler tekst basert spill
## Om Prosjektet
Spillet er en tekst basert dungeon crawler som fungerer ved at du går gjennom rom i en dungeon og møter på fiender du kan ha kamp med. Beseirer du et rom blir du belønnet med et tilfeldig gear, enten rustning eller våpen. Målet er å prøve å komme så langt som mulig og beseire flest mulig fiender.

## Hvordan fungerer spillet
Helt til å begynne med så får man lage navn til karakteren sin før noe mer skjer.

Så blir det generert et rom med et tilfeldig antall fiender basert på global difficulty som øker når man spiller gjennom. Etter det går man inn i kamp fasen for første fiende, hvor man får valg om å angripe eller flykte, flykter man så ender man spillet og får info om hvor mange fiender man drepte. Velger man å angripe så gjør man skade på fienden og den gjør skade på deg, basert på noen tilfeldige variabler, det er en mulighet for å få critical hit på fienden, varierer mellom våpen. Når du beseirer en fiende går du videre til neste helt til rommet er tømt, da går man til loot fasen. Da får man en tilfeldig loot fra loot table, 50/50 om det er våpen eller rustning, og hva man får deretter er basert på en funksjon som gir forskjellige sjanser til forskjellige items. Så får man valge om å beholde itemen eller gå videre. Våpen øker foreløpig bare skade og crit chance, mens rustning reduserer skade man tar fra fiender. Dør man i kamp så avslutter spillet på samme måte som om man flykter.

## KI bruk
Har skrevet nesten alt av kode for hånd selv, har fått hjelp med hvordan å løse noen småting, for eksempel dictionary for loot tables, der kom AI med en god løsning når jeg satt litt fast. Utenom det har jeg brukt mye KI for feilsøking, vært flere ganger jeg satt fast på en feilmelding for så å spørre KI og innse at jeg skrev en variabel feil eller en annen idiotisk feil, spart mye tid på det. 



