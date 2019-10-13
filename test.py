
src = {"minecraftgame", "intelligent", "innercrafttalent", "knife", "scissor", "stonecrafter"}
key = "craft"
result = []

for text in src:
    if text.__contains__(key):
        result.append(text)

print (result)