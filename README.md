Hvad består systemet af?
1. Book-klassen – Bøgerne i biblioteket
Denne klasse repræsenterer en bog og holder styr på følgende:

book_id: Et unikt ID for bogen.

title: Bogens titel.

author: Forfatterens navn.

copies: Hvor mange eksemplarer der er tilgængelige.

Nyttige metoder:

display_info(): Viser info om bogen.

update_book(...): Giver mulighed for at opdatere titel, forfatter og antal kopier – du bestemmer selv hvilke felter.

2. Member-klassen – Brugere af biblioteket
Denne klasse bruges til at repræsentere de personer, der låner bøger.

member_id: Unikt ID.

name: Navn på medlemmet.

password: Bruges som adgangskode.

borrowed_books: En liste over bøger, medlemmet har lånt.

Vigtige metoder:

verify_password(): Bruger bliver bedt om adgangskode.

display_info(): Viser medlem og deres lån.

borrow_books(...): Forsøger at låne bøger (viser fejl hvis ingen eksemplarer er ledige).

return_books(...): Returnerer bøger, hvis de findes i lånelisten.

3. Library-klassen – Systemets kerne
Her sker al organiseringen – fra at holde styr på bøger og brugere til at håndtere udlån.

books: Liste over alle bøger.

members: Liste over alle medlemmer.

Centrale metoder:

add_book(...) / remove_book(...): Tilføj eller fjern bøger.

add_member(...) / remove_member(...): Tilføj eller fjern brugere.

choose_action(...): Start brugerhandlinger (efter adgangskode).

issue_books(...) / return_books(...): Lån og returnering.

display_books() / display_members(): Viser overblik.

run(): Hovedmenuen – herfra styres hele oplevelsen.

Adgangskodebeskyttelse

For at beskytte brugernes lånedata, kræves adgangskode ved låne/retur-handlinger. Hvis adgangskoden er forkert, stoppes processen, og brugeren får besked.


Sådan foregår lån og returnering
Lån af bøger:

Systemet viser alle tilgængelige bøger.

Brugeren indtaster ID'er eller titler på de bøger, de vil låne.

Systemet opdaterer beholdningen og føjer bogen til brugerens liste.

Returnering:

Systemet viser kun de bøger, brugeren har lånt.

Brugeren vælger hvilke, der skal returneres.

Lageret opdateres, og bogen fjernes fra lånelisten.

Menu og brugerinput
Når programmet kører, ser menuen sådan ud:

 Library Menu 
1. Vis alle bøger
2. Vis alle medlemmer
3. Tilføj en bog
4. Fjern en bog
5. Tilføj et medlem
6. Fjern et medlem
7. Medlemsfunktioner (lån/retur)
8. Afslut
Alle valg foretages ved at indtaste et tal fra 1 til 8.

Eksempel: Tilføj en bog

Enter book ID: 4
Enter title: Artificial Intelligence
Enter author: Alan Turing
Enter number of copies: 2

Fejlhåndtering
Hvis du taster noget forkert (f.eks. bogstaver i stedet for tal), bliver det fanget med try/except.

Systemet giver besked, hvis en bog eller et medlem ikke findes.

Brugeren får altid mulighed for at prøve igen, indtil der er indtastet noget gyldigt.
