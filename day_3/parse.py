def parse_args_or_none(part):
    # if it doesn't start with a '(', we know this is not valid
    if not part.startswith('('):
        return None

    # at this point, we know it starts with a '(' so we can ignore that
    # character and split on the closing paren to separate the arguments into
    # the first element of the resulting list. We know if there aren't at
    # least two elements, we have an invalid expression
    maybe_args = part[1:].split(')')
    if len(maybe_args) < 2:
        return None
    
    # we only care about the first element, as it contains the arguments if
    # there are any
    maybe_args = maybe_args[0]
    # here we know we at least have something resembling "(?)"", so let's split
    # on the comma and check for whether we have the right number of arguments
    maybe_args = maybe_args.split(',')
    if len(maybe_args) != 2:
        return None

    # now try turning the arguments into numbers or return None if that fails
    try:
        return tuple(int(arg) for arg in maybe_args)
    except ValueError:
        return None