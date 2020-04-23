
# 2020.4/23.thurs, by Vivy Chen(Queen)

# str.ljust()
# https://www.runoob.com/python/att-string-ljust.html

# str.rjust()
# https://www.runoob.com/python/att-string-rjust.html

# str.zfill()
# https://www.runoob.com/python/att-string-zfill.html

# type() == isinstance()
# https://www.runoob.com/python/python-func-isinstance.html
        

def string_len(length, key, name, fill = False):

    def valid(val):
        if fill:
            val = str(val).ljust(length)
        value_len = len(str(val))

        if value_len != length:
            raise ValueError("{}({}) format err ({})".format(name, key, length))

        return str(val)

    return valid #???

#-------------------------------------------------------------

def int_len(length, key, name, fill = False):

    def valid(val):
        try:
            if not isinstance(int(val), int):
                raise ValueError("{}({}) format err ({})".format(name, key, length))
        except ValueError:
            raise ValueError("{}({}) format err ({})".format(name, key, length))

        if fill:
            val = str(val).zfill(length)

        value_len = len((val))

        if value_len != length or val.isdigit() != True:
            raise ValueError("{}({}) format err ({})".format(name, key, length))

        return str(val)

    return valid #???

#-------------------------------------------------------------

def float_len(length, scale, key, name):

    def valid(val):

        try:
            val = float(val)
            if not isinstance(val, float):
                raise ValueError("{}({}) format err ( ({}) ({}))".format(name, key, length - scale, scale))
            if len(str(val).replace('.', '')) > length:
                raise ValueError("{}({}) format err ( ({}) ({}))".format(name, key, length - scale, scale))
        except ValueError:
            raise ValueError("{}({}) format err ( ({}) ({}))".format(name, key, length - scale, scale))
        
        # if value >= math.pow(10, (length - scale)):
        #     raise ValueError("{}({}) 格式錯誤 (({}) ({}))".format(name, key, length - scale, scale))
        # else:
        #     value = ('%.4f' % (value)).replace('.', '').zfill(9)

        return str(val)

    return valid #???

    