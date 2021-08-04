from Stack import ArrayStack

def is_matched(expr):
    lefty = "<({["  # opening delimiters
    righty = ">)}]"  # respective closing delims
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)  # push left delimiter on stack

        if c in righty:
            S.push(c)

    if S.bottom() in lefty and S.top() in righty:
        if lefty.index(S.bottom()) == righty.index(S.top()):
            return True
    else:
        return False
    return S.isEmpty()