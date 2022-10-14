
# can you change the self parameter inside a class something else(say'harry'.try changing self to 'slf' or 'mittal' and see the effects.
class self:
    def __init__(mittal,pre):
        mittal.pre=pre
sel=self('hey')
print(sel.pre)

# yes it will work if we write mittal instade of self.