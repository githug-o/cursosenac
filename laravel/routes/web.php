<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\Controller;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/', [Controller::class,'lista'])->name('index');
Route::get('inputs', [Controller::class,'criarendereco'])->name('inputs');
Route::get('editar/{id}', [Controller::class,'editar'])->name('editar');
Route::post('update/{id}', [Controller::class,'update'])->name('update');
Route::get('deletar/{id}', [Controller::class,'deletar'])->name('deletar');
Route::post('criar/endereco',[Controller::class,'criar'])->name('criar');

