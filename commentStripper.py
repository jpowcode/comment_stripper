from optparse import OptionParser
import time
import os
import re


def find_file_type(infile):
    file_type = infile.split('.')[1]
    extensions = {'py': 'python', 'pyc': 'python',
                  'c': 'c', 'cpp': 'c++', 'cxx': 'c++', 'cXX': 'c++',
                  'lhs': 'haskell', 'hs': 'haskell',
                  'js': 'js',
                  'html': 'html',
                  'rc': 'rust',
                  'clj': 'clojure', 'cljs': 'clojure', 'cljc': 'clojure',
                  'edn': 'clojure',
                  'pl': 'perl'}
    return extensions[file_type]


def check_time(filename):
    current_time = time.time()
    file_time = os.stat(filename).st_mtime
    if current_time - file_time < 5:
        return True
    else:
        return False


def gen_strip(infile, outfile,
              sing_line_com, multi_line_com_start,
              multi_line_com_end, comment_no_text,
              end_line_com, end_line_com_id):

    f_in = open(infile, 'r')
    f_out = open(outfile, 'w')
    long_com = False

    for line in f_in:
        com = False

        if sing_line_com.match(line):
            com = True

        elif end_line_com.match(line):
            com = True
            f_out.write(line.split(end_line_com_id)[0])
            f_out.write('\n')

        else:
            if multi_line_com_start is not None:
                if comment_no_text.match(line):
                    if long_com is False:
                        long_com = True

                    else:
                        long_com = False
                        com = True

                if multi_line_com_start.match(line) and long_com is False:
                    long_com = True

                if multi_line_com_end.match(line) and long_com is True:
                    long_com = False
                    com = True

        if not (long_com or com):
            f_out.write(line)

    f_in.close()
    f_out.close()


def strip_python(infile, outfile):
    sing_line_com = re.compile('^#(.*)|^"""(.*)"""$')
    multi_line_com_start = re.compile('^"""(.+)')
    multi_line_com_end = re.compile('(.+)"""$')
    comment_no_text = re.compile('^"""$')
    end_line_com = re.compile('^(.+)#(.*)')
    end_line_com_id = '#'

    gen_strip(infile, outfile,
              sing_line_com, multi_line_com_start,
              multi_line_com_end, comment_no_text,
              end_line_com, end_line_com_id)


def strip_c(infile, outfile):
    sing_line_com = re.compile('^/\*(.+)\*/$')
    multi_line_com_start = re.compile('^/\*(.+)')
    multi_line_com_end = re.compile('(.+)\*/$')
    comment_no_text = re.compile('^/\*$|^\*/$')
    end_line_com = re.compile('(.+)/\*(.*)\*/')
    end_line_com_id = '/*'

    gen_strip(infile, outfile,
              sing_line_com, multi_line_com_start,
              multi_line_com_end, comment_no_text,
              end_line_com, end_line_com_id)


def strip_js(infile, outfile):
    sing_line_com = re.compile('^//(.*)$')
    multi_line_com_start = re.compile('^/\*(.+)')
    multi_line_com_end = re.compile('(.+)\*/$')
    comment_no_text = re.compile('^/\*$|^\*/$')
    end_line_com = re.compile('(.+)//(.*)\*/')
    end_line_com_id = '//'

    gen_strip(infile, outfile,
              sing_line_com, multi_line_com_start,
              multi_line_com_end, comment_no_text,
              end_line_com, end_line_com_id)


def strip_cpp(infile, outfile):
    sing_line_com = re.compile('^//(.*)$')
    multi_line_com_start = re.compile('^/\*(.+)')
    multi_line_com_end = re.compile('(.+)\*/$')
    comment_no_text = re.compile('^/\*$|^\*/$')
    end_line_com = re.compile('(.+)//(.*)\*/')
    end_line_com_id = '//'

    gen_strip(infile, outfile,
              sing_line_com, multi_line_com_start,
              multi_line_com_end, comment_no_text,
              end_line_com, end_line_com_id)


def strip_haskell(infile, outfile):
    sing_line_com = re.compile('^{-(.+)-}|--(.*)$')
    multi_line_com_start = re.compile('^{-(.+)')
    multi_line_com_end = re.compile('(.+)-}$')
    comment_no_text = re.compile('^{-$|^-}$')
    end_line_com = re.compile('(.+){-(.*)-}')
    end_line_com_id = '{-'

    gen_strip(infile, outfile,
              sing_line_com, multi_line_com_start,
              multi_line_com_end, comment_no_text,
              end_line_com, end_line_com_id)


def strip_clojure(infile, outfile):
    sing_line_com = re.compile('^;(.+)$')
    multi_line_com_start = re.compile('^\(comment "(.+)')
    multi_line_com_end = re.compile('(.+)"\)$')
    comment_no_text = re.compile('^\(comment "$|^"\)$')
    end_line_com = re.compile('(.+);(.*)')
    end_line_com_id = ';'

    gen_strip(infile, outfile,
              sing_line_com, multi_line_com_start,
              multi_line_com_end, comment_no_text,
              end_line_com, end_line_com_id)


def strip_rust(infile, outfile):
    sing_line_com = re.compile('^//(.*)$')
    multi_line_com_start = None
    multi_line_com_end = None
    comment_no_text = None
    end_line_com = re.compile('(.+)//(.*)')
    end_line_com_id = '//'

    gen_strip(infile, outfile,
              sing_line_com, multi_line_com_start,
              multi_line_com_end, comment_no_text,
              end_line_com, end_line_com_id)


def strip_perl(infile, outfile):
    sing_line_com = re.compile('^#(.*)$')
    multi_line_com_start = None
    multi_line_com_end = None
    comment_no_text = None
    end_line_com = re.compile('(.+)//(.*)')
    end_line_com_id = '//'

    gen_strip(infile, outfile,
              sing_line_com, multi_line_com_start,
              multi_line_com_end, comment_no_text,
              end_line_com, end_line_com_id)


def strip_html(infile, outfile):
    sing_line_com = re.compile('^<!--(.+)-->$')
    multi_line_com_start = re.compile('^<!--(.+)')
    multi_line_com_end = re.compile('(.+)-->$')
    comment_no_text = re.compile('^<!--$|^-->$')
    end_line_com = re.compile('(.+)<!--(.*)-->')
    end_line_com_id = '<!--'

    gen_strip(infile, outfile,
              sing_line_com, multi_line_com_start,
              multi_line_com_end, comment_no_text,
              end_line_com, end_line_com_id)


def strip_files(infile, outfile):
    file_type = find_file_type(infile)

    if file_type == 'python':
        strip_python(infile, outfile)

    if file_type == 'c':
        strip_c(infile, outfile)

    if file_type == 'c++':
        strip_cpp(infile, outfile)

    if file_type == 'haskell':
        strip_haskell(infile, outfile)

    if file_type == 'clojure':
        strip_clojure(infile, outfile)

    if file_type == 'rust':
        strip_rust(infile, outfile)

    if file_type == 'html':
        strip_html(infile, outfile)

    if file_type == 'js':
        strip_js(infile, outfile)

    if file_type == 'perl':
        strip_perl(infile, outfile)

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-i", "--in", action="store", type="string",
                      dest="infile",
                      help="""specify a comma separated list of files to strip
                      from comments, no spaces between names""")

    parser.add_option("-o", "--out", action="store", type="string",
                      dest="outfile",
					  help="""specify a comma separatd list of output file,
                      no spaces between names""")

    parser.add_option("-w", "--watch", action="store_true", dest="watch",
					  help="sets the programme into realtime watching mode")

    (options, args) = parser.parse_args()
    infiles = options.infile.split(',')
    outfiles = options.outfile.split(',')

    if options.watch:
        while True:
            time.sleep(5)
            for i in range(len(infiles)):
                if check_time(infiles[i]):

                    strip_files(infiles[i], outfiles[i])

    else:
        for i in range(len(infiles)):
            strip_files(infiles[i], outfiles[i])
