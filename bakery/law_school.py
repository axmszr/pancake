
class Painter:
    GRN = "G"
    YLW = "Y"
    GRY = "R"

    def colour(g, a):
        if len(g) != len(a):
            raise Exception("Words not of same length: " + \
                            f"{g} [{len(g)}] vs. {a} [{len(a)}]")
        l = len(g)
        new_g = g.upper()
        new_a = a.upper()

        match = tuple(new_g[i] == new_a[i] for i in range(l))
        remain = [new_a[i] for i in range(l) if not match[i]]

        out = []
        for i in range(l):
            if match[i]:
                out.append(Painter.GRN)
            elif new_g[i] in remain:
                out.append(Painter.YLW)
                remain.remove(new_g[i])
            else:
                out.append(Painter.GRY)

        return ''.join(out)

    def is_match(g, a, col):
        return Painter.colour(g, a) == col.upper()

    def unicode(c):
        match c:
            case Painter.GRN:
                return "\U0001F7E9"
            case Painter.YLW:
                return "\U0001F7E8"
            case Painter.GRY:
                return "\U00002B1C"
            case _:
                raise Exception(f"Invalid colour symbol: {c}.")

    def emojify(col):
        codes = [Painter.unicode(c) for c in col]
        return ''.join(codes)
