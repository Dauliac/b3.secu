# Security
Thierry Meyer - 2018

---
## Ethique
Meme si on à tout les privilèges sur une donnée on en est pas le propriétaire

Lois francaise:
*Autour de la cyber criminalité*

cyber criminalité: Désigne l'ensseble des infractions pénales, suceptibles de se commettres sur les réseaux de télécom ou ciblant ces memes réseaux.

=> 2 réalités:
    - Infractions spécifiques:
        Atteintes au S.T.A.D: Système de traitement automatisé de données: Article 323-[1-n] de code pénal
        Modifié par la lois n°2015-912  du 24/07/2015 art 4:
            - Le fait d'acceder ou de se maintenir frauduleusement dans tout ou partie d'un S.T.A.D,
              est punis de 2 ans d'emprisonement et de 60 000 d'amende.
            - Le fait de supprimer ou de modifier des datas dans un SI,
              La peine est portée à 3 ans de prisons et 100 000 d'amendes.
            - Lorsque les infractions commises prévue par les 2 premiers alinéas,
              dans le cadre d'un carractère personnel,
              la peine est portée à 5 ans et 150 000 d'amende.
            - Les atteintes au droits des personnes au fichiers,
              ou au personne sont dans les articles: 226-16 à 226-24 du code pénal.
    - Infractions est liée ou facilité par l'usage des T.I.C:
      - Les atteintes au mineurs, articles 227-23 du code pénal
      - Les infractions sur l presse 24/07/1881sécurité
      - Les atteintes au personnes (menaces,  usurpation d'identité, ...)
      - Les escroqueries phishing, fausses loteries,
        utilisations frauduleuse de moyens permanent.

## Intro Sécurité du SI
###SI:
> Enssemble organisé de ressource qui permet de regrouper,
> classifier, traiter et diffuser de l'info sur un env donné.

### Sécurité du SI:
> L'ensseble des moyens techniques, juridiques, organisationnels, humains, mis en place permettant de garantir:
> la confidentialité, l'intégrité, et la disponibilité.

Critères de sécurité:
- confidentialité: Guarantir que la ressource est limité au entité authorisées.
- intégrité: Propriété, protection, l'exactitude, l'exaustivité de l'actif.
- disponibilité: Accessible et utilisable à l ademmande par une entité authorisée.

On doit appliquer ces mesures à tout les niveaux.
> Principe de défense en profondeur
Il n'y à pas de solution de défense générique
> Il n'y à jamais 100% de sécutité.
=> amener le risque à un niveau acceptable

Actif: tout ce qui à de la valeur pour l'organisation
Vul: Failles dans un actif
Menance: Cause potentielle d'un évènement indésirable

Vraisseblance: crédence en la possibilité de réalisation d'un évènement.
Conséquence: résultat du sénario
Impact: changement radical des actifs touchés.

## Mots de passe
```
cat /etc/shadow
user:$A$S....$H.....:
     | $x type de hash:
       | Sel
             | Hash
```
Algo de hash:
- $1: md5
- $6: SHA512


Bonne mesure:
Ajouter un sel:
MD5(xorg(pass, salt))

