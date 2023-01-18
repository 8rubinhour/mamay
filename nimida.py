def func1(arg1, arg2):
    var62 = var5(arg1, arg2)
    var63 = -1058907127 ^ (-737 + ((arg2 ^ 189 & -326) | arg2) - arg2 + arg1 + arg2) + -506 - ((var62 ^ (795 ^ -946088890 & 925)) ^ ((var62 ^ arg2) + (-1790212006 + 1092464242)))
    var64 = (var62 + (var63 + arg1 - arg2)) ^ 965
    result = var63 ^ -2135740632 | var64
    return result
def func4(arg6, arg7):
    def func5(arg8, arg9):
        var14 = func6(arg8, arg9)
        var20 = func7(arg8, arg6)
        var24 = func8(var20, arg7)
        var25 = arg8 - var20
        var26 = arg6 - var25 - var14 | var24
        var27 = arg7 + -62 + arg8
        var28 = var14 + (var24 + -369) + arg6
        var29 = arg8 & var27 - var25 + arg7
        var30 = (73181156 ^ arg8) & var29 - arg8
        var31 = var25 | var24
        var32 = var25 - var28
        var33 = var31 ^ arg6
        var34 = -2127069020 & var28 + var30 ^ var27
        var35 = var27 | (var28 | var30 ^ -1154532606)
        if var32 < arg6:
            var36 = var34 & var26 ^ var24 - var24
        else:
            var36 = ((var20 - var35) + arg8) | var33
        var37 = var20 + (var27 - var24)
        if var33 < arg6:
            var38 = var31 - var32
        else:
            var38 = var14 - var30 ^ var14
        if var34 < var32:
            var39 = (var24 + arg6) - arg9 + var33
        else:
            var39 = (arg7 & var20) + var32 & var27
        if var29 < arg8:
            var40 = 1372624053 & var37 - var31
        else:
            var40 = arg6 + arg8
        result = arg9 & var35 ^ (var25 | 983) | var27 ^ var14 & var14
        return result
    var41 = func5(arg6, arg7)
    var42 = ((arg7 | 782959182) & arg6) & 367460319
    var43 = (arg6 | arg6) ^ 840 + var41
    var44 = var42 + -853734505 + (arg7 - 1920934809)
    var45 = arg6 | (474 ^ arg6 + var42)
    var46 = arg6 & var41 - var45 & arg6
    var47 = (var41 + var45 - var46) ^ arg6
    var48 = (arg6 & var47) - 351 + var42
    var49 = arg6 | var42 ^ var41 ^ var42
    var50 = (var41 | var48) - var41 | var48
    var51 = var44 - arg6 | var49 ^ var43
    var52 = var45 ^ var45 ^ var46 | var42
    var53 = ((var45 & var52) ^ var44) + var45
    var54 = ((var42 & var45) & var46) & var41
    var55 = var48 + var49
    var56 = var41 & var49 - var50
    if var54 < var48:
        var57 = var52 - var55
    else:
        var57 = (415 | var47 + var55) - 718
    var58 = (var56 + (996 - var44)) | var43
    var59 = var56 + var43 ^ var46 - var48
    var60 = (var54 & var43) - var42 ^ var50
    var61 = (var47 | arg7) | var55 & var44
    result = (var49 ^ var52) & (var44 - (arg6 ^ var41 | (var45 + (arg6 ^ var49 - var50 ^ var59)))) + var60 + arg7
    return result
def func7(arg15, arg16):
    var17 = arg15 | 292 - arg15 - 402
    var18 = arg15 | -2027862548
    var19 = -328 - 804863980 | var17 ^ (var18 - (var17 & (arg15 | var17) & ((arg16 - (811 | arg15) & ((arg15 - (arg15 - 2117094100) | arg15) + var17 | 343 - (2006255093 + arg15 - arg15) + arg15) + -236) - -1854014635)))
    result = arg15 | var18
    return result
def func6(arg10, arg11):
    var12 = 0
    for var13 in range(7):
        if var13 < arg10:
            var12 += var13 | arg11 | -2
        else:
            var12 += (arg10 & var13) ^ var12
    return var12
def func3():
    closure = [9]
    def func2(arg3, arg4):
        closure[0] += func4(arg3, arg4)
        return closure[0]
    func = func2
    return func
var5 = func3()
def func8(arg21, arg22):
    def func9(acc, rest):
        var23 = -4 & rest ^ acc
        if acc == 0:
            return var23
        else:
            result = func9(acc - 1, var23)
            return result
    result = func9(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 10'
    print 'arg_number: 65'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
