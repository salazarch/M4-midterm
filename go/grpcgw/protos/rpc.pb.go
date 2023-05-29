// Code generated by protoc-gen-go. DO NOT EDIT.
// source: rpc.proto

package rest_gw

import (
	fmt "fmt"
	proto "github.com/golang/protobuf/proto"
	_ "google.golang.org/genproto/googleapis/api/annotations"
	_ "google.golang.org/protobuf/types/known/emptypb"
	math "math"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion3 // please upgrade the proto package

type Coords struct {
	Values               []float64 `protobuf:"fixed64,1,rep,packed,name=values,proto3" json:"values,omitempty"`
	XXX_NoUnkeyedLiteral struct{}  `json:"-"`
	XXX_unrecognized     []byte    `json:"-"`
	XXX_sizecache        int32     `json:"-"`
}

func (m *Coords) Reset()         { *m = Coords{} }
func (m *Coords) String() string { return proto.CompactTextString(m) }
func (*Coords) ProtoMessage()    {}
func (*Coords) Descriptor() ([]byte, []int) {
	return fileDescriptor_77a6da22d6a3feb1, []int{0}
}

func (m *Coords) XXX_Unmarshal(b []byte) error {
	return xxx_messageInfo_Coords.Unmarshal(m, b)
}
func (m *Coords) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	return xxx_messageInfo_Coords.Marshal(b, m, deterministic)
}
func (m *Coords) XXX_Merge(src proto.Message) {
	xxx_messageInfo_Coords.Merge(m, src)
}
func (m *Coords) XXX_Size() int {
	return xxx_messageInfo_Coords.Size(m)
}
func (m *Coords) XXX_DiscardUnknown() {
	xxx_messageInfo_Coords.DiscardUnknown(m)
}

var xxx_messageInfo_Coords proto.InternalMessageInfo

func (m *Coords) GetValues() []float64 {
	if m != nil {
		return m.Values
	}
	return nil
}

func init() {
	proto.RegisterType((*Coords)(nil), "RPCPkg.Coords")
}

func init() { proto.RegisterFile("rpc.proto", fileDescriptor_77a6da22d6a3feb1) }

var fileDescriptor_77a6da22d6a3feb1 = []byte{
	// 212 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xe2, 0xe2, 0x2c, 0x2a, 0x48, 0xd6,
	0x2b, 0x28, 0xca, 0x2f, 0xc9, 0x17, 0x62, 0x0b, 0x0a, 0x70, 0x0e, 0xc8, 0x4e, 0x97, 0x92, 0x4e,
	0xcf, 0xcf, 0x4f, 0xcf, 0x49, 0xd5, 0x07, 0x8b, 0x26, 0x95, 0xa6, 0xe9, 0xa7, 0xe6, 0x16, 0x94,
	0x54, 0x42, 0x14, 0x49, 0xc9, 0x40, 0x25, 0x13, 0x0b, 0x32, 0xf5, 0x13, 0xf3, 0xf2, 0xf2, 0x4b,
	0x12, 0x4b, 0x32, 0xf3, 0xf3, 0x8a, 0x21, 0xb2, 0x4a, 0x2a, 0x5c, 0x6c, 0xce, 0xf9, 0xf9, 0x45,
	0x29, 0xc5, 0x42, 0x52, 0x5c, 0x6c, 0x65, 0x89, 0x39, 0xa5, 0xa9, 0xc5, 0x12, 0x8c, 0x0a, 0xcc,
	0x1a, 0x8c, 0x4e, 0x4c, 0x02, 0x8c, 0x41, 0x50, 0x11, 0xa3, 0x78, 0x2e, 0xe6, 0xa0, 0x00, 0x67,
	0xa1, 0x08, 0x2e, 0x0e, 0xf7, 0xd4, 0x12, 0xb0, 0x7a, 0x21, 0x31, 0x3d, 0x88, 0xb9, 0x7a, 0x30,
	0x4b, 0xf5, 0x5c, 0x41, 0x96, 0x4a, 0xf1, 0xe9, 0x41, 0x1c, 0xa5, 0x07, 0x31, 0x56, 0x49, 0xa5,
	0xe9, 0xf2, 0x93, 0xc9, 0x4c, 0x72, 0x4a, 0x92, 0xfa, 0x45, 0xa9, 0xc5, 0x25, 0xe9, 0x89, 0x25,
	0xa9, 0xe5, 0x89, 0x95, 0x29, 0xa9, 0xb9, 0xf9, 0xfa, 0xe9, 0xa9, 0x25, 0xc9, 0x20, 0x35, 0x56,
	0x8c, 0x5a, 0x4e, 0xa2, 0x51, 0xc2, 0x20, 0x69, 0xdd, 0xf4, 0x72, 0xbd, 0xe4, 0xfc, 0x5c, 0x7d,
	0x28, 0x3b, 0x89, 0x0d, 0x6c, 0xb8, 0x31, 0x20, 0x00, 0x00, 0xff, 0xff, 0x1f, 0x1b, 0x58, 0xc3,
	0xf4, 0x00, 0x00, 0x00,
}