color = ["red", "orange", "green", "violet", "blue", "yellow"]

def Colors(color_list, n):
    colors = color_list.copy()
    colors = colors[:n]
    return colors

for i in range(len(Colors(color, 6))):
    print(Colors(color, 6)[:i+1])

tekst = "Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli. "

tekst = tekst.split(sep = " ")[1:12]

tekst[0] = tekst[0].strip("(")
tekst[-1] = tekst[-1].strip(")")

x = ""
for i in range(len(tekst)):
    x = x + tekst[i] + " "
print(x)

definition = "Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli. "

print(definition[definition.index('(')+1:definition.index(')')])
