{
  description = "A basic Nix flake with Go devShell";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-26.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        devShells.default = pkgs.mkShell {
          packages = with pkgs; [
            gnumake
            go
            golangci-lint
            gopls
            gotools
            openapi-generator-cli
            openapi-python-client
            tree-sitter
            tree-sitter-grammars.tree-sitter-go
          ];
        };
      }
    );
}
