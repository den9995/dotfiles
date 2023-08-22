vim.g.mapleader= " "
vim.keymap.set("n","<leader>fe",vim.cmd.Ex)

-- greatest remap ever
vim.keymap.set("x", "<leader>p", [["_dP]])

-- next greatest remap ever : asbjornHaland
vim.keymap.set({"n", "v"}, "<leader>y", [["+y]])
vim.keymap.set("n", "<leader>Y", [["+Y]])

vim.keymap.set({"n", "v"}, "<leader>d", [["_d]])

vim.keymap.set("n", "<leader><leader>", function()
    vim.cmd("so")
end)

vim.keymap.set("n", "<leader>s", [[:%s/\<<C-r><C-w>\>/<C-r><C-w>/gI<Left><Left><Left>]])
vim.keymap.set("n", "<leader>x", "<cmd>!chmod +x %<CR>", { silent = true })

vim.keymap.set("n",    "<C-S>", ":w"            )
vim.keymap.set("n",    "<leader>j", ":tabp<CR>" )
vim.keymap.set("n",    "<leader>k", ":tabn<CR>" )
vim.keymap.set("n",    "<leader>nt", ":tabe ."  )
--vim.keymap.set("n",    "<A-j>", ":tabp<CR>"     )
--vim.keymap.set("n",    "<A-k>", ":tabn<CR>"     )
vim.keymap.set("t", "<A-h>",  "<C-\\><C-N><C-w>h")
vim.keymap.set("t", "<A-j>",  "<C-\\><C-N><C-w>j")
vim.keymap.set("t", "<A-k>",  "<C-\\><C-N><C-w>k")
vim.keymap.set("t", "<A-l>",  "<C-\\><C-N><C-w>l")
vim.keymap.set("i", "<A-h>",  "<C-\\><C-N><C-w>h")
vim.keymap.set("i", "<A-j>",  "<C-\\><C-N><C-w>j")
vim.keymap.set("i", "<A-k>",  "<C-\\><C-N><C-w>k")
vim.keymap.set("i", "<A-l>",  "<C-\\><C-N><C-w>l")
vim.keymap.set("n", "<A-h>",  "<C-w>h"           )
vim.keymap.set("n", "<A-j>",  "<C-w>j"           )
vim.keymap.set("n", "<A-k>",  "<C-w>k"           )
vim.keymap.set("n", "<A-l>",  "<C-w>l"           )
vim.keymap.set("n", "<CA-h>", "<C-w>H"           )
vim.keymap.set("n", "<CA-j>", "<C-w>J"           )
vim.keymap.set("n", "<CA-k>", "<C-w>K"           )
vim.keymap.set("n", "<CA-l>", "<C-w>L"           )
vim.keymap.set("t", "<Esc>",  "<C-\\><C-n>"      )

vim.keymap.set("n",    "<leader>r", ":w |! ./run.sh "   )
vim.keymap.set("n",    "<leader>th", ":abo vsp | term<CR>") --left split term
vim.keymap.set("n",    "<leader>tj", ":bel  sp | term<CR>") --down  split term
vim.keymap.set("n",    "<leader>tk", ":abo  sp | term<CR>") --up split term
vim.keymap.set("n",    "<leader>tl", ":bel vsp | term<CR>") --right split term
--vim.keymap.set("n",    "<leader>t", ":vsp |<C-w>l|:term<CR>i")
vim.keymap.set("n",    "<leader>vh", ":abo vsp <CR>") --left split
vim.keymap.set("n",    "<leader>vj", ":bel  sp <CR>") --down  split
vim.keymap.set("n",    "<leader>vk", ":abo  sp <CR>") --up split
vim.keymap.set("n",    "<leader>vl", ":bel vsp <CR>") --right split
