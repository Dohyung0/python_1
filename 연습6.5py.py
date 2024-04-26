def rep_char(c,n):
    print(c*n)

def draw_line_string(prompt):
    l = len(prompt)
    rep_char('-',l*2+4)
    print(f'  {prompt}')
    rep_char('-',l*2+4)
    
draw_line_string('안녕하세요')
