import string
from collections import Counter
import matplotlib.pyplot as plt

# Liste plus complète de stop words à ignorer
STOP_WORDS = set(["a","abord","absolument","afin","ah","ai","aie","aient","aies","ailleurs","ainsi","ait","allaient","allo","allons","allô","alors","anterieur","anterieure","anterieures","apres","après","as","assez","attendu","au","aucun","aucune","aucuns","aujourd","aujourd'hui","aupres","auquel","aura","aurai","auraient","aurais","aurait","auras","aurez","auriez","aurions","aurons","auront","aussi","autant","autre","autrefois","autrement","autres","autrui","aux","auxquelles","auxquels","avaient","avais","avait","avant","avec","avez","aviez","avions","avoir","avons","ayant","ayez","ayons","b","bah","bas","basee","bat","beau","beaucoup","bien","bigre","bon","boum","bravo","brrr","c","car","ce","ceci","cela","celle","celle-ci","celle-là","celles","celles-ci","celles-là","celui","celui-ci","celui-là","celà","cent","cependant","certain","certaine","certaines","certains","certes","ces","cet","cette","ceux","ceux-ci","ceux-là","chacun","chacune","chaque","cher","chers","chez","chiche","chut","chère","chères","ci","cinq","cinquantaine","cinquante","cinquantième","cinquième","clac","clic","combien","comme","comment","comparable","comparables","compris","concernant","contre","couic","crac","d","da","dans","de","debout","dedans","dehors","deja","delà","depuis","dernier","derniere","derriere","derrière","des","desormais","desquelles","desquels","dessous","dessus","deux","deuxième","deuxièmement","devant","devers","devra","devrait","different","differentes","differents","différent","différente","différentes","différents","dire","directe","directement","dit","dite","dits","divers","diverse","diverses","dix","dix-huit","dix-neuf","dix-sept","dixième","doit","doivent","donc","dont","dos","douze","douzième","dring","droite","du","duquel","durant","dès","début","désormais","e","effet","egale","egalement","egales","eh","elle","elle-même","elles","elles-mêmes","en","encore","enfin","entre","envers","environ","es","essai","est","et","etant","etc","etre","eu","eue","eues","euh","eurent","eus","eusse","eussent","eusses","eussiez","eussions","eut","eux","eux-mêmes","exactement","excepté","extenso","exterieur","eûmes","eût","eûtes","f","fais","faisaient","faisant","fait","faites","façon","feront","fi","flac","floc","fois","font","force","furent","fus","fusse","fussent","fusses","fussiez","fussions","fut","fûmes","fût","fûtes","g","gens","h","ha","haut","hein","hem","hep","hi","ho","holà","hop","hormis","hors","hou","houp","hue","hui","huit","huitième","hum","hurrah","hé","hélas","i","ici","il","ils","importe","j","je","jusqu","jusque","juste","k","l","la","laisser","laquelle","las","le","lequel","les","lesquelles","lesquels","leur","leurs","longtemps","lors","lorsque","lui","lui-meme","lui-même","là","lès","m","ma","maint","maintenant","mais","malgre","malgré","maximale","me","meme","memes","merci","mes","mien","mienne","miennes","miens","mille","mince","mine","minimale","moi","moi-meme","moi-même","moindres","moins","mon","mot","moyennant","multiple","multiples","même","mêmes","n","na","naturel","naturelle","naturelles","ne","neanmoins","necessaire","necessairement","neuf","neuvième","ni","nombreuses","nombreux","nommés","non","nos","notamment","notre","nous","nous-mêmes","nouveau","nouveaux","nul","néanmoins","nôtre","nôtres","o","oh","ohé","ollé","olé","on","ont","onze","onzième","ore","ou","ouf","ouias","oust","ouste","outre","ouvert","ouverte","ouverts","o|","où","p","paf","pan","par","parce","parfois","parle","parlent","parler","parmi","parole","parseme","partant","particulier","particulière","particulièrement","pas","passé","pendant","pense","permet","personne","personnes","peu","peut","peuvent","peux","pff","pfft","pfut","pif","pire","pièce","plein","plouf","plupart","plus","plusieurs","plutôt","possessif","possessifs","possible","possibles","pouah","pour","pourquoi","pourrais","pourrait","pouvait","prealable","precisement","premier","première","premièrement","pres","probable","probante","procedant","proche","près","psitt","pu","puis","puisque","pur","pure","q","qu","quand","quant","quant-à-soi","quanta","quarante","quatorze","quatre","quatre-vingt","quatrième","quatrièmement","que","quel","quelconque","quelle","quelles","quelqu'un","quelque","quelques","quels","qui","quiconque","quinze","quoi","quoique","r","rare","rarement","rares","relative","relativement","remarquable","rend","rendre","restant","reste","restent","restrictif","retour","revoici","revoilà","rien","s","sa","sacrebleu","sait","sans","sapristi","sauf","se","sein","seize","selon","semblable","semblaient","semble","semblent","sent","sept","septième","sera","serai","seraient","serais","serait","seras","serez","seriez","serions","serons","seront","ses","seul","seule","seulement","si","sien","sienne","siennes","siens","sinon","six","sixième","soi","soi-même","soient","sois","soit","soixante","sommes","son","sont","sous","souvent","soyez","soyons","specifique","specifiques","speculatif","stop","strictement","subtiles","suffisant","suffisante","suffit","suis","suit","suivant","suivante","suivantes","suivants","suivre","sujet","superpose","sur","surtout","t","ta","tac","tandis","tant","tardive","te","tel","telle","tellement","telles","tels","tenant","tend","tenir","tente","tes","tic","tien","tienne","tiennes","tiens","toc","toi","toi-même","ton","touchant","toujours","tous","tout","toute","toutefois","toutes","treize","trente","tres","trois","troisième","troisièmement","trop","très","tsoin","tsouin","tu","té","u","un","une","unes","uniformement","unique","uniques","uns","v","va","vais","valeur","vas","vers","via","vif","vifs","vingt","vivat","vive","vives","vlan","voici","voie","voient","voilà","voire","vont","vos","votre","vous","vous-mêmes","vu","vé","vôtre","vôtres","w","x","y","z","zut","à","â","ça","ès","étaient","étais","était","étant","état","étiez","étions","été","étée","étées","étés","êtes","être","ô"])

def nettoyer_texte(texte):
    texte = texte.lower()
    texte = texte.translate(str.maketrans("", "", string.punctuation))
    return texte

def stats_generales(texte):
    mots = texte.split()
    nb_mots = len(mots)
    nb_caracteres = len(texte)
    nb_caracteres_sans_espace = len(texte.replace(" ", ""))
    nb_phrases = texte.count('.') + texte.count('!') + texte.count('?')
    longueur_moyenne_mots = sum(len(m) for m in mots) / nb_mots if nb_mots else 0

    print("\n--- Statistiques Générales ---")
    print(f"Nombre de mots: {nb_mots}")
    print(f"Nombre de phrases: {nb_phrases}")
    print(f"Nombre de caractères (avec espaces): {nb_caracteres}")
    print(f"Nombre de caractères (sans espaces): {nb_caracteres_sans_espace}")
    print(f"Longueur moyenne des mots: {longueur_moyenne_mots:.2f}")

def mots_frequents(texte, n=10):
    mots = texte.split()
    mots_filtrés = [m for m in mots if m not in STOP_WORDS]
    compte = Counter(mots_filtrés)
    
    # Demande combien de mots afficher dans le top
    top_n = input(f"Combien de mots afficher dans le top ? (default {n}): ")
    top_n = int(top_n) if top_n.isdigit() else n

    plus_frequents = compte.most_common(top_n)

    print(f"\n--- Top {top_n} mots les plus fréquents ---")
    for mot, freq in plus_frequents:
        print(f"{mot}: {freq}")

    # Graphique
    mots_graph = [m for m, _ in plus_frequents]
    freqs_graph = [f for _, f in plus_frequents]

    # Ajuste la taille de la figure selon le nombre de mots
    largeur = max(15, len(mots_graph) * 0.5)  # plus large si beaucoup de mots
    plt.figure(figsize=(largeur, 8))  # taille grande mais pas bloquante
    
    plt.bar(mots_graph, freqs_graph, color='skyblue')
    plt.title(f"Top {top_n} mots les plus fréquents", fontsize=16)
    plt.xlabel("Mots", fontsize=14)
    plt.ylabel("Fréquence", fontsize=14)
    
    # Rotation des étiquettes pour lisibilité
    plt.xticks(rotation=45, ha='right', fontsize=12)
    
    plt.tight_layout()  # ajuste tout correctement
    plt.show()


def rechercher_mot(texte):
    mot = input("\nEntrer le mot à rechercher: ").lower()
    mots = texte.split()
    count = mots.count(mot)
    print(f"Le mot '{mot}' apparaît {count} fois.")

def main():
    print("=== Analyseur de Texte avec Graphique Amélioré ===")
    choix = input("1. Lire un fichier texte\n2. Entrer du texte manuellement\nChoix: ")

    if choix == "1":
        chemin = input("Chemin du fichier texte: ")
        try:
            with open(chemin, "r", encoding="utf-8") as f:
                texte = f.read()
        except FileNotFoundError:
            print("Fichier non trouvé !")
            return
    else:
        texte = input("Entrez votre texte:\n")

    texte_nettoye = nettoyer_texte(texte)
    stats_generales(texte_nettoye)
    mots_frequents(texte_nettoye)
    rechercher_mot(texte_nettoye)

if __name__ == "__main__":
    main()
