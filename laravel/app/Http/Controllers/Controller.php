<?php

namespace App\Http\Controllers;

use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Routing\Controller as BaseController;
use App\Models\Endereco;
use Illuminate\Http\Request;
use App\Models\Cliente;

class Controller extends BaseController
{
    use AuthorizesRequests, ValidatesRequests;

    public function criarendereco(){
        return view("welcome");
    }
    public function criar(Request $request){
        $endereco =  new Endereco();
        $endereco->cep = $request->input("cep");
        $endereco->uf = $request->input("uf");
        $endereco->cidade = $request->input("cidade");
        $endereco->bairro = $request->input("bairro");
        $endereco->rua = $request->input("rua");
        $endereco->numero = $request->input("numero");
        $endereco->complemento = $request->input("complemento");
        $endereco->save();
        
        $cliente =  new Cliente();
        $cliente->nome = $request->input("nome");
        $cliente->email = $request->input("email");
        $cliente->telefone = $request->input("telefone");
        $cliente->endereco_id = $endereco->id;
        $cliente->save();
        
        return redirect("/")->with("success", "Cadastro realizado com sucesso!");

    }
    public function lista(){
        $cliente=Cliente::join('endereco', 'cliente.endereco_id', '=', 'endereco.id')
        ->select('cliente.id', 'cliente.nome', 'cliente.email', 'cliente.telefone',
                  'endereco.cidade', 'endereco.cep', 'endereco.uf', 'endereco.rua',
                  'endereco.bairro', 'endereco.numero', 'endereco.complemento')
        ->get();

        return view("lista", compact("cliente"));
    }

    public function editar($id){
        $cliente=Cliente::join('endereco', 'cliente.endereco_id', '=', 'endereco.id')
            ->select('cliente.id', 'cliente.nome', 'cliente.email', 'cliente.telefone',
                'endereco.cidade', 'endereco.cep', 'endereco.uf', 'endereco.rua',
                'endereco.bairro', 'endereco.numero', 'endereco.complemento')
            ->where('cliente.id', '=',$id)
        ->get();

        return view("editar", compact("cliente"));        
    }

    public function update(Request $request, $id){
        $cliente = Cliente::find($id);
        $cliente->nome = $request->input("nome");
        $cliente->email = $request->input("email");
        $cliente->telefone = $request->input("telefone");
        $cliente->update();    

        $endereco = Endereco::find($cliente->endereco_id);
        $endereco->cep = $request->input("cep");
        $endereco->uf = $request->input("uf");
        $endereco->cidade = $request->input("cidade");
        $endereco->bairro = $request->input("bairro");
        $endereco->rua = $request->input("rua");
        $endereco->numero = $request->input("numero");
        $endereco->complemento = $request->input("complemento");
        $endereco->update();

        return redirect("/")->with("success", "Cadastro atualizado com sucesso!");
        
    }

    public function deletar($id){
        $cliente = Cliente::find($id);
        $endereco = Endereco::find($id);
        $cliente->delete();
        $endereco->delete();

        return redirect("/")->with("success", "Cadastro excluído com sucesso!");
    }

}