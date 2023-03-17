
import re
import sys

def search_text(infile = 'origin.txt', 
                outfile = 'origin_output.txt', 
                terms = ['herit']):

    """
    Extracts the line number and word from the document located at the 
    path infile that are matched from a list of search terms provided 
    (or defaults if nothing is provided). 
    
    The values are written to an output file that is provided in the 
    variable outfile. The search is not case insensitive.

    PARAMETERS
    ----------
    infile : str
        The path to the input file to be searched.
    outfile : str
        The path to the output file to be written to.
    terms : list
        A list of terms to search for in the input file.
    
    RETURNS
    -------
    None
    """

    # Create a regular expression pattern from the list of terms
    pattern = "[A-Z]*(" + '|'.join(terms) + ")[A-Z]*" #join the words with a pipe to create pattern
    REpattern = re.compile(pattern, re.IGNORECASE) #compile the pattern
    print('Opening ' + infile) #print the input file
    with open(infile, 'r') as in_stream: #open the input file
        print('Opening ' + outfile) #print the output file
        with open(outfile, 'w') as out_stream: #open the output file
            print('Searching ' + infile + ' for ' + pattern + '...')
            for count, line in enumerate(in_stream): #for each line in the input file
                if re.search(REpattern, line): #if the pattern is found in the line
                    word = re.search(REpattern, line).group() #find the word
                    output = "Line: " + str(count) + " Word: " + word #create the output
                    out_stream.write('{0}\n'.format(output)) #write the output to the output file
    print("Done!")
    print(infile +  ' is closed?', in_stream.closed)
    print(outfile + ' is closed?', out_stream.closed, '\n')

def main():
    import argparse

    default_terms = ['herit'] #words to search for
    default_infile = 'origin.txt' #input file
    default_outfile = 'origin_output.txt' #output file

    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--infile',    
            type=str,
            default= None,
            help=('input file to be searched. ' 
                  'default: origin.txt'))
    parser.add_argument('-o', '--outfile', 
            type=str,
            default= None,
            help=('output file to be written to. '
                  'default: origin_output.txt'))
    parser.add_argument('-t', '--terms',
            type=str,
            default= None,
            help=('list of terms used to search the input file. ' 
                  'terms are separated by spaces. '
                  'default: [heritable, inherit, inheritance]'))
    # Parse the command-line arguments into a 'dict'-like container
    args = parser.parse_args()

    # Check to see if outfile was provided by the caller. If not,
    # use the defaults.
    if not args.outfile:
        args.outfile = default_outfile

    # Check to see if terms was provided by the caller. If not,
    # use the defaults.
    if not args.terms:
        args.terms = default_terms
    else:
        args.terms = args.terms.split() 

    # Check to see if infile was provided by the caller. If not,
    # use the defaults.    
    if not args.infile:
        args.infile = default_infile 

    #Return the input file, output file, and terms
    print('infile: ', args.infile, '\noutfile: ', args.outfile, '\nterms: ', args.terms, '\n')

    # Call the search_text function   
    search_text(infile = args.infile, 
                outfile = args.outfile, 
                terms = args.terms)

if __name__ == '__main__':
    main()