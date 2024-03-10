# # move n plates from src to dest
# def move(n, src, tmp, dest):
#     print("move %d from %c to %c" % (n, src, tmp, dest))

# move(3, 'a', 'b', 'c')

# Move n plates from src to dest
def move(n, src, tmp, dest):
    if n == 1:
        print("move 1 from", src, "to", dest)
        return
    move(n-1, src, dest, tmp)
    print("move", n, "from", src, "to", dest)
    move(n-1, tmp, src, dest)

move(3, 'a', 'b', 'c')