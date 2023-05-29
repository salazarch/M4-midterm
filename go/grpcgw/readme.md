//go install github.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-grpc-gateway
//go install github.com/grpc-ecosystem/grpc-gateway/v2/protoc-gen-openapiv2
//go install google.golang.org/protobuf/cmd/protoc-gen-go
//go install google.golang.org/grpc/cmd/protoc-gen-go-grpc
//protoc -I ./protos -I /home/izacs/data/devel/googleapis --go_out ./protos --go_opt paths=source_relative --go-grpc_out ./protos --go-grpc_opt paths=source_relative rpc.proto
//protoc -I ./protos -I /home/izacs/data/devel/googleapis --plugin=protoc-gen-grpc-gateway=/home/izacs/tools/gw/protoc-gen-grpc-gateway-v2.15.2-linux-x86_64 --grpc-gateway_out ./protos --grpc-gateway_opt logtostderr=true --grpc-gateway_opt paths=source_relative rpc.proto
protoc -I ./protos --grpc-gateway_out ./protos --grpc-gateway_opt logtostderr=true --grpc-gateway_opt paths=source_relative rpc.proto
//alternative for gw: protoc -I ./protos --grpc-gateway_out ./protos --grpc-gateway_opt logtostderr=true --grpc-gateway_opt paths=source_relative rpc.proto