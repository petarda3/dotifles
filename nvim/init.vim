" Neovim commands
:set number
:set relativenumber
:set autoindent
:set tabstop=4
:set shiftwidth=4
:set smarttab
:set softtabstop=4
:set mouse=a
:set textwidth=80
:set fo+=t
colorscheme solarized

" Neovim plugins
call plug#begin()
Plug 'https://github.com/tpope/vim-surround' " Surround word with cs something
Plug 'https://github.com/preservim/nerdtree' " NerdTree
Plug 'https://github.com/tpope/vim-commentary' " Comment line-gcc & Comment paragrap-gcap 
Plug 'https://github.com/vim-airline/vim-airline' " Status bar
Plug 'https://github.com/ap/vim-css-color' " CSS Color Preview
Plug 'https://github.com/rafi/awesome-vim-colorschemes' " Retro Scheme
Plug 'https://github.com/jiangmiao/auto-pairs' " Auto close bracket
Plug 'https://github.com/vim-airline/vim-airline-themes' " Themes for status bar
Plug 'https://github.com/preservim/tagbar' " Tags for imports, variables etc...
call plug#end()


" Configuration for NerdTree
let g:NERDTreeDirArrowExpandable="+"
let g:NERDTreeDirArrowCollapsible="~"


" Keybindings
nnoremap <C-f> :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-q> :<CMD>q!<CR>
nnoremap <C-w> :update<CR>
nmap <F8> :TagbarToggle<CR>

" Status bar configuration
let g:airline_theme='base16_solarized_dark'
let g:airline_powerline_fonts = 1

if !exists('g:airline_symbols')
  let g:airline_symbols = {}
endif

let g:airline_section_z = '%3 row=%l:col=%c'
let g:airline_left_sep = ''
let g:airline_left_alt_sep = ''
let g:airline_right_sep = ''
let g:airline_right_alt_sep = ''
let g:airline_symbols.readonly = ''

