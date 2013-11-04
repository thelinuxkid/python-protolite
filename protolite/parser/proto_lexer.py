# $ANTLR 3.1.3 Mar 18, 2009 10:09:25 proto_lexer.g 2013-10-23 04:20:51

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EXPONENT=60
MESSAGE_LITERAL=11
REQUIRED_PROTOBUF_SCOPE_LITERAL=29
STRING_GUTS=54
EQUALS=25
UINT32_PROTOBUF_TYPE_LITERAL=37
INT32_PROTOBUF_TYPE_LITERAL=35
EOF=-1
UINT64_PROTOBUF_TYPE_LITERAL=38
QUALIFIED_IDENTIFIER=63
ESCAPE_SEQUENCE=56
UNICODE_ESCAPE=58
FIXED64_PROTOBUF_TYPE_LITERAL=42
STRING_LITERAL=55
PACKAGE_LITERAL=7
FIXED32_PROTOBUF_TYPE_LITERAL=41
COMMA=27
IDENTIFIER=62
EXTEND_LITERAL=12
REPEATED_PROTOBUF_SCOPE_LITERAL=31
PROTOBUF_TYPE_LITERAL=48
ENUM_LITERAL=10
IMPORT_LITERAL=8
HEX_LITERAL=49
COMMENT=5
FLOAT_PROTOBUF_TYPE_LITERAL=34
BYTES_PROTOBUF_TYPE_LITERAL=47
BLOCK_OPEN=19
SFIXED64_PROTOBUF_TYPE_LITERAL=44
SERVICE_LITERAL=16
PROTOBUF_SCOPE_LITERAL=32
END_OF_LINE=4
EXTENSIONS_TO_LITERAL=14
OPTIONAL_PROTOBUF_SCOPE_LITERAL=30
PAREN_CLOSE=22
BOOL_PROTOBUF_TYPE_LITERAL=45
ITEM_TERMINATOR=28
OCTAL_LITERAL=50
EXTENSIONS_MAX_LITERAL=15
OPTION_LITERAL=9
HEX_DIGIT=53
STRING_PROTOBUF_TYPE_LITERAL=46
WHITESPACE=6
OCTAL_ESCAPE=57
BOOL_LITERAL=59
EXTENSIONS_DEF_LITERAL=13
SINT32_PROTOBUF_TYPE_LITERAL=39
FLOAT_LITERAL=61
COLON=26
BLOCK_CLOSE=20
INT64_PROTOBUF_TYPE_LITERAL=36
FIELD_IDENTIFIER=64
INTEGER_LITERAL=52
PAREN_OPEN=21
DOUBLE_PROTOBUF_TYPE_LITERAL=33
SFIXED32_PROTOBUF_TYPE_LITERAL=43
DECIMAL_LITERAL=51
BRACKET_CLOSE=24
SINT64_PROTOBUF_TYPE_LITERAL=40
RPC_LITERAL=18
RETURNS_LITERAL=17
BRACKET_OPEN=23


class proto_lexer(Lexer):

    grammarFileName = "proto_lexer.g"
    antlr_version = version_str_to_tuple("3.1.3 Mar 18, 2009 10:09:25")
    antlr_version_str = "3.1.3 Mar 18, 2009 10:09:25"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(proto_lexer, self).__init__(input, state)


        self.dfa7 = self.DFA7(
            self, 7,
            eot = self.DFA7_eot,
            eof = self.DFA7_eof,
            min = self.DFA7_min,
            max = self.DFA7_max,
            accept = self.DFA7_accept,
            special = self.DFA7_special,
            transition = self.DFA7_transition
            )

        self.dfa29 = self.DFA29(
            self, 29,
            eot = self.DFA29_eot,
            eof = self.DFA29_eof,
            min = self.DFA29_min,
            max = self.DFA29_max,
            accept = self.DFA29_accept,
            special = self.DFA29_special,
            transition = self.DFA29_transition
            )

        self.dfa35 = self.DFA35(
            self, 35,
            eot = self.DFA35_eot,
            eof = self.DFA35_eof,
            min = self.DFA35_min,
            max = self.DFA35_max,
            accept = self.DFA35_accept,
            special = self.DFA35_special,
            transition = self.DFA35_transition
            )




              
    literals = dict([
        ("PACKAGE_LITERAL", "package"),
        ("IMPORT_LITERAL", "import"),
        ("OPTION_LITERAL", "option"),
        ("ENUM_LITERAL", "enum"),
        ("MESSAGE_LITERAL", "message"),
        ("EXTEND_LITERAL", "extend"),
        ("EXTENSIONS_DEF_LITERAL", "extensions"),
        ("EXTENSIONS_TO_LITERAL", "to"),
        ("EXTENSIONS_MAX_LITERAL", "max"),
        ("SERVICE_LITERAL", "service"),
        ("RETURNS_LITERAL", "returns"),
        ("RPC_LITERAL", "rpc"),
        ("BLOCK_OPEN", "{"),
        ("BLOCK_CLOSE", "}"),
        ("PAREN_OPEN", "("),
        ("PAREN_CLOSE", ")"),
        ("BRACKET_OPEN", "["),
        ("BRACKET_CLOSE", "]"),
        ("EQUALS", "="),
        ("COLON", ":"),
        ("COMMA", ","),
        ("ITEM_TERMINATOR", ";"),
    ])

    def getLiterals():
        return literals;



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):

        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:39:3: ( '//' (~ ( '\\n' | '\\r' ) )* END_OF_LINE | '/*' ( options {greedy=false; } : . )* '*/' )
            alt3 = 2
            LA3_0 = self.input.LA(1)

            if (LA3_0 == 47) :
                LA3_1 = self.input.LA(2)

                if (LA3_1 == 47) :
                    alt3 = 1
                elif (LA3_1 == 42) :
                    alt3 = 2
                else:
                    nvae = NoViableAltException("", 3, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 3, 0, self.input)

                raise nvae

            if alt3 == 1:
                # proto_lexer.g:39:6: '//' (~ ( '\\n' | '\\r' ) )* END_OF_LINE
                pass 
                self.match("//")
                # proto_lexer.g:39:11: (~ ( '\\n' | '\\r' ) )*
                while True: #loop1
                    alt1 = 2
                    LA1_0 = self.input.LA(1)

                    if ((0 <= LA1_0 <= 9) or (11 <= LA1_0 <= 12) or (14 <= LA1_0 <= 65535)) :
                        alt1 = 1


                    if alt1 == 1:
                        # proto_lexer.g:39:11: ~ ( '\\n' | '\\r' )
                        pass 
                        if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 65535):
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse



                    else:
                        break #loop1
                self.mEND_OF_LINE()
                #action start
                self.skip()
                #action end


            elif alt3 == 2:
                # proto_lexer.g:40:6: '/*' ( options {greedy=false; } : . )* '*/'
                pass 
                self.match("/*")
                # proto_lexer.g:40:11: ( options {greedy=false; } : . )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 == 42) :
                        LA2_1 = self.input.LA(2)

                        if (LA2_1 == 47) :
                            alt2 = 2
                        elif ((0 <= LA2_1 <= 46) or (48 <= LA2_1 <= 65535)) :
                            alt2 = 1


                    elif ((0 <= LA2_0 <= 41) or (43 <= LA2_0 <= 65535)) :
                        alt2 = 1


                    if alt2 == 1:
                        # proto_lexer.g:40:38: .
                        pass 
                        self.matchAny()


                    else:
                        break #loop2
                self.match("*/")
                #action start
                self.skip()
                #action end


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "END_OF_LINE"
    def mEND_OF_LINE(self, ):

        try:
            # proto_lexer.g:42:21: ( '\\r\\n' | '\\n' | '\\r' | )
            alt4 = 4
            LA4 = self.input.LA(1)
            if LA4 == 13:
                LA4_1 = self.input.LA(2)

                if (LA4_1 == 10) :
                    alt4 = 1
                else:
                    alt4 = 3
            elif LA4 == 10:
                alt4 = 2
            else:
                alt4 = 4
            if alt4 == 1:
                # proto_lexer.g:42:23: '\\r\\n'
                pass 
                self.match("\r\n")


            elif alt4 == 2:
                # proto_lexer.g:42:32: '\\n'
                pass 
                self.match(10)


            elif alt4 == 3:
                # proto_lexer.g:42:39: '\\r'
                pass 
                self.match(13)


            elif alt4 == 4:
                # proto_lexer.g:42:46: 
                pass 
                #action start
                self.skip()
                #action end



        finally:

            pass

    # $ANTLR end "END_OF_LINE"



    # $ANTLR start "WHITESPACE"
    def mWHITESPACE(self, ):

        try:
            _type = WHITESPACE
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:43:12: ( ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+ )
            # proto_lexer.g:43:14: ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+
            pass 
            # proto_lexer.g:43:14: ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+
            cnt5 = 0
            while True: #loop5
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((9 <= LA5_0 <= 10) or (12 <= LA5_0 <= 13) or LA5_0 == 32) :
                    alt5 = 1


                if alt5 == 1:
                    # proto_lexer.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or (12 <= self.input.LA(1) <= 13) or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt5 >= 1:
                        break #loop5

                    eee = EarlyExitException(5, self.input)
                    raise eee

                cnt5 += 1
            #action start
            self.skip()
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WHITESPACE"



    # $ANTLR start "PACKAGE_LITERAL"
    def mPACKAGE_LITERAL(self, ):

        try:
            _type = PACKAGE_LITERAL
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:45:17: ( 'package' )
            # proto_lexer.g:45:19: 'package'
            pass 
            self.match("package")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PACKAGE_LITERAL"



    # $ANTLR start "IMPORT_LITERAL"
    def mIMPORT_LITERAL(self, ):

        try:
            _type = IMPORT_LITERAL
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:46:16: ( 'import' )
            # proto_lexer.g:46:18: 'import'
            pass 
            self.match("import")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IMPORT_LITERAL"



    # $ANTLR start "OPTION_LITERAL"
    def mOPTION_LITERAL(self, ):

        try:
            _type = OPTION_LITERAL
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:47:16: ( 'option' )
            # proto_lexer.g:47:18: 'option'
            pass 
            self.match("option")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OPTION_LITERAL"



    # $ANTLR start "ENUM_LITERAL"
    def mENUM_LITERAL(self, ):

        try:
            _type = ENUM_LITERAL
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:49:14: ( 'enum' )
            # proto_lexer.g:49:16: 'enum'
            pass 
            self.match("enum")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ENUM_LITERAL"



    # $ANTLR start "MESSAGE_LITERAL"
    def mMESSAGE_LITERAL(self, ):

        try:
            _type = MESSAGE_LITERAL
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:50:17: ( 'message' )
            # proto_lexer.g:50:19: 'message'
            pass 
            self.match("message")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "MESSAGE_LITERAL"



    # $ANTLR start "EXTEND_LITERAL"
    def mEXTEND_LITERAL(self, ):

        try:
            _type = EXTEND_LITERAL
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:51:16: ( 'extend' )
            # proto_lexer.g:51:18: 'extend'
            pass 
            self.match("extend")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EXTEND_LITERAL"



    # $ANTLR start "EXTENSIONS_DEF_LITERAL"
    def mEXTENSIONS_DEF_LITERAL(self, ):

        try:
            _type = EXTENSIONS_DEF_LITERAL
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:52:24: ( 'extensions' )
            # proto_lexer.g:52:26: 'extensions'
            pass 
            self.match("extensions")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EXTENSIONS_DEF_LITERAL"



    # $ANTLR start "EXTENSIONS_TO_LITERAL"
    def mEXTENSIONS_TO_LITERAL(self, ):

        try:
            _type = EXTENSIONS_TO_LITERAL
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:53:23: ( 'to' )
            # proto_lexer.g:53:25: 'to'
            pass 
            self.match("to")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EXTENSIONS_TO_LITERAL"



    # $ANTLR start "EXTENSIONS_MAX_LITERAL"
    def mEXTENSIONS_MAX_LITERAL(self, ):

        try:
            _type = EXTENSIONS_MAX_LITERAL
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:54:24: ( 'max' )
            # proto_lexer.g:54:26: 'max'
            pass 
            self.match("max")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EXTENSIONS_MAX_LITERAL"



    # $ANTLR start "SERVICE_LITERAL"
    def mSERVICE_LITERAL(self, ):

        try:
            _type = SERVICE_LITERAL
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:61:17: ( 'service' )
            # proto_lexer.g:61:19: 'service'
            pass 
            self.match("service")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "SERVICE_LITERAL"



    # $ANTLR start "RETURNS_LITERAL"
    def mRETURNS_LITERAL(self, ):

        try:
            _type = RETURNS_LITERAL
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:62:17: ( 'returns' )
            # proto_lexer.g:62:19: 'returns'
            pass 
            self.match("returns")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RETURNS_LITERAL"



    # $ANTLR start "RPC_LITERAL"
    def mRPC_LITERAL(self, ):

        try:
            _type = RPC_LITERAL
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:63:13: ( 'rpc' )
            # proto_lexer.g:63:15: 'rpc'
            pass 
            self.match("rpc")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "RPC_LITERAL"



    # $ANTLR start "BLOCK_OPEN"
    def mBLOCK_OPEN(self, ):

        try:
            _type = BLOCK_OPEN
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:65:12: ( '{' )
            # proto_lexer.g:65:14: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BLOCK_OPEN"



    # $ANTLR start "BLOCK_CLOSE"
    def mBLOCK_CLOSE(self, ):

        try:
            _type = BLOCK_CLOSE
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:66:13: ( '}' )
            # proto_lexer.g:66:15: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BLOCK_CLOSE"



    # $ANTLR start "PAREN_OPEN"
    def mPAREN_OPEN(self, ):

        try:
            _type = PAREN_OPEN
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:67:12: ( '(' )
            # proto_lexer.g:67:14: '('
            pass 
            self.match(40)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PAREN_OPEN"



    # $ANTLR start "PAREN_CLOSE"
    def mPAREN_CLOSE(self, ):

        try:
            _type = PAREN_CLOSE
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:68:13: ( ')' )
            # proto_lexer.g:68:15: ')'
            pass 
            self.match(41)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PAREN_CLOSE"



    # $ANTLR start "BRACKET_OPEN"
    def mBRACKET_OPEN(self, ):

        try:
            _type = BRACKET_OPEN
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:69:14: ( '[' )
            # proto_lexer.g:69:16: '['
            pass 
            self.match(91)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BRACKET_OPEN"



    # $ANTLR start "BRACKET_CLOSE"
    def mBRACKET_CLOSE(self, ):

        try:
            _type = BRACKET_CLOSE
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:70:15: ( ']' )
            # proto_lexer.g:70:17: ']'
            pass 
            self.match(93)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BRACKET_CLOSE"



    # $ANTLR start "EQUALS"
    def mEQUALS(self, ):

        try:
            _type = EQUALS
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:71:8: ( '=' )
            # proto_lexer.g:71:10: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EQUALS"



    # $ANTLR start "COLON"
    def mCOLON(self, ):

        try:
            _type = COLON
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:72:7: ( ':' )
            # proto_lexer.g:72:9: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COLON"



    # $ANTLR start "COMMA"
    def mCOMMA(self, ):

        try:
            _type = COMMA
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:73:7: ( ',' )
            # proto_lexer.g:73:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMA"



    # $ANTLR start "ITEM_TERMINATOR"
    def mITEM_TERMINATOR(self, ):

        try:
            _type = ITEM_TERMINATOR
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:74:17: ( ';' )
            # proto_lexer.g:74:19: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ITEM_TERMINATOR"



    # $ANTLR start "PROTOBUF_SCOPE_LITERAL"
    def mPROTOBUF_SCOPE_LITERAL(self, ):

        try:
            _type = PROTOBUF_SCOPE_LITERAL
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:78:3: ( REQUIRED_PROTOBUF_SCOPE_LITERAL | OPTIONAL_PROTOBUF_SCOPE_LITERAL | REPEATED_PROTOBUF_SCOPE_LITERAL )
            alt6 = 3
            LA6_0 = self.input.LA(1)

            if (LA6_0 == 114) :
                LA6_1 = self.input.LA(2)

                if (LA6_1 == 101) :
                    LA6_3 = self.input.LA(3)

                    if (LA6_3 == 113) :
                        alt6 = 1
                    elif (LA6_3 == 112) :
                        alt6 = 3
                    else:
                        nvae = NoViableAltException("", 6, 3, self.input)

                        raise nvae

                else:
                    nvae = NoViableAltException("", 6, 1, self.input)

                    raise nvae

            elif (LA6_0 == 111) :
                alt6 = 2
            else:
                nvae = NoViableAltException("", 6, 0, self.input)

                raise nvae

            if alt6 == 1:
                # proto_lexer.g:78:6: REQUIRED_PROTOBUF_SCOPE_LITERAL
                pass 
                self.mREQUIRED_PROTOBUF_SCOPE_LITERAL()


            elif alt6 == 2:
                # proto_lexer.g:79:6: OPTIONAL_PROTOBUF_SCOPE_LITERAL
                pass 
                self.mOPTIONAL_PROTOBUF_SCOPE_LITERAL()


            elif alt6 == 3:
                # proto_lexer.g:80:6: REPEATED_PROTOBUF_SCOPE_LITERAL
                pass 
                self.mREPEATED_PROTOBUF_SCOPE_LITERAL()


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PROTOBUF_SCOPE_LITERAL"



    # $ANTLR start "REQUIRED_PROTOBUF_SCOPE_LITERAL"
    def mREQUIRED_PROTOBUF_SCOPE_LITERAL(self, ):

        try:
            # proto_lexer.g:83:42: ( 'required' )
            # proto_lexer.g:83:44: 'required'
            pass 
            self.match("required")




        finally:

            pass

    # $ANTLR end "REQUIRED_PROTOBUF_SCOPE_LITERAL"



    # $ANTLR start "OPTIONAL_PROTOBUF_SCOPE_LITERAL"
    def mOPTIONAL_PROTOBUF_SCOPE_LITERAL(self, ):

        try:
            # proto_lexer.g:84:42: ( 'optional' )
            # proto_lexer.g:84:44: 'optional'
            pass 
            self.match("optional")




        finally:

            pass

    # $ANTLR end "OPTIONAL_PROTOBUF_SCOPE_LITERAL"



    # $ANTLR start "REPEATED_PROTOBUF_SCOPE_LITERAL"
    def mREPEATED_PROTOBUF_SCOPE_LITERAL(self, ):

        try:
            # proto_lexer.g:85:42: ( 'repeated' )
            # proto_lexer.g:85:44: 'repeated'
            pass 
            self.match("repeated")




        finally:

            pass

    # $ANTLR end "REPEATED_PROTOBUF_SCOPE_LITERAL"



    # $ANTLR start "PROTOBUF_TYPE_LITERAL"
    def mPROTOBUF_TYPE_LITERAL(self, ):

        try:
            _type = PROTOBUF_TYPE_LITERAL
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:90:3: ( DOUBLE_PROTOBUF_TYPE_LITERAL | FLOAT_PROTOBUF_TYPE_LITERAL | INT32_PROTOBUF_TYPE_LITERAL | INT64_PROTOBUF_TYPE_LITERAL | UINT32_PROTOBUF_TYPE_LITERAL | UINT64_PROTOBUF_TYPE_LITERAL | SINT32_PROTOBUF_TYPE_LITERAL | SINT64_PROTOBUF_TYPE_LITERAL | FIXED32_PROTOBUF_TYPE_LITERAL | FIXED64_PROTOBUF_TYPE_LITERAL | SFIXED32_PROTOBUF_TYPE_LITERAL | SFIXED64_PROTOBUF_TYPE_LITERAL | BOOL_PROTOBUF_TYPE_LITERAL | STRING_PROTOBUF_TYPE_LITERAL | BYTES_PROTOBUF_TYPE_LITERAL )
            alt7 = 15
            alt7 = self.dfa7.predict(self.input)
            if alt7 == 1:
                # proto_lexer.g:90:6: DOUBLE_PROTOBUF_TYPE_LITERAL
                pass 
                self.mDOUBLE_PROTOBUF_TYPE_LITERAL()


            elif alt7 == 2:
                # proto_lexer.g:91:6: FLOAT_PROTOBUF_TYPE_LITERAL
                pass 
                self.mFLOAT_PROTOBUF_TYPE_LITERAL()


            elif alt7 == 3:
                # proto_lexer.g:92:6: INT32_PROTOBUF_TYPE_LITERAL
                pass 
                self.mINT32_PROTOBUF_TYPE_LITERAL()


            elif alt7 == 4:
                # proto_lexer.g:93:6: INT64_PROTOBUF_TYPE_LITERAL
                pass 
                self.mINT64_PROTOBUF_TYPE_LITERAL()


            elif alt7 == 5:
                # proto_lexer.g:94:6: UINT32_PROTOBUF_TYPE_LITERAL
                pass 
                self.mUINT32_PROTOBUF_TYPE_LITERAL()


            elif alt7 == 6:
                # proto_lexer.g:95:6: UINT64_PROTOBUF_TYPE_LITERAL
                pass 
                self.mUINT64_PROTOBUF_TYPE_LITERAL()


            elif alt7 == 7:
                # proto_lexer.g:96:6: SINT32_PROTOBUF_TYPE_LITERAL
                pass 
                self.mSINT32_PROTOBUF_TYPE_LITERAL()


            elif alt7 == 8:
                # proto_lexer.g:97:6: SINT64_PROTOBUF_TYPE_LITERAL
                pass 
                self.mSINT64_PROTOBUF_TYPE_LITERAL()


            elif alt7 == 9:
                # proto_lexer.g:98:6: FIXED32_PROTOBUF_TYPE_LITERAL
                pass 
                self.mFIXED32_PROTOBUF_TYPE_LITERAL()


            elif alt7 == 10:
                # proto_lexer.g:99:6: FIXED64_PROTOBUF_TYPE_LITERAL
                pass 
                self.mFIXED64_PROTOBUF_TYPE_LITERAL()


            elif alt7 == 11:
                # proto_lexer.g:100:6: SFIXED32_PROTOBUF_TYPE_LITERAL
                pass 
                self.mSFIXED32_PROTOBUF_TYPE_LITERAL()


            elif alt7 == 12:
                # proto_lexer.g:101:6: SFIXED64_PROTOBUF_TYPE_LITERAL
                pass 
                self.mSFIXED64_PROTOBUF_TYPE_LITERAL()


            elif alt7 == 13:
                # proto_lexer.g:102:6: BOOL_PROTOBUF_TYPE_LITERAL
                pass 
                self.mBOOL_PROTOBUF_TYPE_LITERAL()


            elif alt7 == 14:
                # proto_lexer.g:103:6: STRING_PROTOBUF_TYPE_LITERAL
                pass 
                self.mSTRING_PROTOBUF_TYPE_LITERAL()


            elif alt7 == 15:
                # proto_lexer.g:104:6: BYTES_PROTOBUF_TYPE_LITERAL
                pass 
                self.mBYTES_PROTOBUF_TYPE_LITERAL()


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PROTOBUF_TYPE_LITERAL"



    # $ANTLR start "DOUBLE_PROTOBUF_TYPE_LITERAL"
    def mDOUBLE_PROTOBUF_TYPE_LITERAL(self, ):

        try:
            # proto_lexer.g:107:39: ( 'double' )
            # proto_lexer.g:107:41: 'double'
            pass 
            self.match("double")




        finally:

            pass

    # $ANTLR end "DOUBLE_PROTOBUF_TYPE_LITERAL"



    # $ANTLR start "FLOAT_PROTOBUF_TYPE_LITERAL"
    def mFLOAT_PROTOBUF_TYPE_LITERAL(self, ):

        try:
            # proto_lexer.g:108:38: ( 'float' )
            # proto_lexer.g:108:40: 'float'
            pass 
            self.match("float")




        finally:

            pass

    # $ANTLR end "FLOAT_PROTOBUF_TYPE_LITERAL"



    # $ANTLR start "INT32_PROTOBUF_TYPE_LITERAL"
    def mINT32_PROTOBUF_TYPE_LITERAL(self, ):

        try:
            # proto_lexer.g:109:38: ( 'int32' )
            # proto_lexer.g:109:40: 'int32'
            pass 
            self.match("int32")




        finally:

            pass

    # $ANTLR end "INT32_PROTOBUF_TYPE_LITERAL"



    # $ANTLR start "INT64_PROTOBUF_TYPE_LITERAL"
    def mINT64_PROTOBUF_TYPE_LITERAL(self, ):

        try:
            # proto_lexer.g:110:38: ( 'int64' )
            # proto_lexer.g:110:40: 'int64'
            pass 
            self.match("int64")




        finally:

            pass

    # $ANTLR end "INT64_PROTOBUF_TYPE_LITERAL"



    # $ANTLR start "UINT32_PROTOBUF_TYPE_LITERAL"
    def mUINT32_PROTOBUF_TYPE_LITERAL(self, ):

        try:
            # proto_lexer.g:111:39: ( 'uint32' )
            # proto_lexer.g:111:41: 'uint32'
            pass 
            self.match("uint32")




        finally:

            pass

    # $ANTLR end "UINT32_PROTOBUF_TYPE_LITERAL"



    # $ANTLR start "UINT64_PROTOBUF_TYPE_LITERAL"
    def mUINT64_PROTOBUF_TYPE_LITERAL(self, ):

        try:
            # proto_lexer.g:112:39: ( 'uint64' )
            # proto_lexer.g:112:41: 'uint64'
            pass 
            self.match("uint64")




        finally:

            pass

    # $ANTLR end "UINT64_PROTOBUF_TYPE_LITERAL"



    # $ANTLR start "SINT32_PROTOBUF_TYPE_LITERAL"
    def mSINT32_PROTOBUF_TYPE_LITERAL(self, ):

        try:
            # proto_lexer.g:113:39: ( 'sint32' )
            # proto_lexer.g:113:41: 'sint32'
            pass 
            self.match("sint32")




        finally:

            pass

    # $ANTLR end "SINT32_PROTOBUF_TYPE_LITERAL"



    # $ANTLR start "SINT64_PROTOBUF_TYPE_LITERAL"
    def mSINT64_PROTOBUF_TYPE_LITERAL(self, ):

        try:
            # proto_lexer.g:114:39: ( 'sint64' )
            # proto_lexer.g:114:41: 'sint64'
            pass 
            self.match("sint64")




        finally:

            pass

    # $ANTLR end "SINT64_PROTOBUF_TYPE_LITERAL"



    # $ANTLR start "FIXED32_PROTOBUF_TYPE_LITERAL"
    def mFIXED32_PROTOBUF_TYPE_LITERAL(self, ):

        try:
            # proto_lexer.g:115:40: ( 'fixed32' )
            # proto_lexer.g:115:42: 'fixed32'
            pass 
            self.match("fixed32")




        finally:

            pass

    # $ANTLR end "FIXED32_PROTOBUF_TYPE_LITERAL"



    # $ANTLR start "FIXED64_PROTOBUF_TYPE_LITERAL"
    def mFIXED64_PROTOBUF_TYPE_LITERAL(self, ):

        try:
            # proto_lexer.g:116:40: ( 'fixed64' )
            # proto_lexer.g:116:42: 'fixed64'
            pass 
            self.match("fixed64")




        finally:

            pass

    # $ANTLR end "FIXED64_PROTOBUF_TYPE_LITERAL"



    # $ANTLR start "SFIXED32_PROTOBUF_TYPE_LITERAL"
    def mSFIXED32_PROTOBUF_TYPE_LITERAL(self, ):

        try:
            # proto_lexer.g:117:41: ( 'sfixed32' )
            # proto_lexer.g:117:43: 'sfixed32'
            pass 
            self.match("sfixed32")




        finally:

            pass

    # $ANTLR end "SFIXED32_PROTOBUF_TYPE_LITERAL"



    # $ANTLR start "SFIXED64_PROTOBUF_TYPE_LITERAL"
    def mSFIXED64_PROTOBUF_TYPE_LITERAL(self, ):

        try:
            # proto_lexer.g:118:41: ( 'sfixed64' )
            # proto_lexer.g:118:43: 'sfixed64'
            pass 
            self.match("sfixed64")




        finally:

            pass

    # $ANTLR end "SFIXED64_PROTOBUF_TYPE_LITERAL"



    # $ANTLR start "BOOL_PROTOBUF_TYPE_LITERAL"
    def mBOOL_PROTOBUF_TYPE_LITERAL(self, ):

        try:
            # proto_lexer.g:119:37: ( 'bool' )
            # proto_lexer.g:119:39: 'bool'
            pass 
            self.match("bool")




        finally:

            pass

    # $ANTLR end "BOOL_PROTOBUF_TYPE_LITERAL"



    # $ANTLR start "STRING_PROTOBUF_TYPE_LITERAL"
    def mSTRING_PROTOBUF_TYPE_LITERAL(self, ):

        try:
            # proto_lexer.g:120:39: ( 'string' )
            # proto_lexer.g:120:41: 'string'
            pass 
            self.match("string")




        finally:

            pass

    # $ANTLR end "STRING_PROTOBUF_TYPE_LITERAL"



    # $ANTLR start "BYTES_PROTOBUF_TYPE_LITERAL"
    def mBYTES_PROTOBUF_TYPE_LITERAL(self, ):

        try:
            # proto_lexer.g:121:38: ( 'bytes' )
            # proto_lexer.g:121:40: 'bytes'
            pass 
            self.match("bytes")




        finally:

            pass

    # $ANTLR end "BYTES_PROTOBUF_TYPE_LITERAL"



    # $ANTLR start "INTEGER_LITERAL"
    def mINTEGER_LITERAL(self, ):

        try:
            _type = INTEGER_LITERAL
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:126:3: ( HEX_LITERAL | OCTAL_LITERAL | DECIMAL_LITERAL )
            alt8 = 3
            LA8 = self.input.LA(1)
            if LA8 == 45:
                LA8_1 = self.input.LA(2)

                if (LA8_1 == 48) :
                    LA8_4 = self.input.LA(3)

                    if (LA8_4 == 88 or LA8_4 == 120) :
                        alt8 = 1
                    elif ((48 <= LA8_4 <= 55)) :
                        alt8 = 2
                    else:
                        nvae = NoViableAltException("", 8, 4, self.input)

                        raise nvae

                elif ((49 <= LA8_1 <= 57)) :
                    alt8 = 3
                else:
                    nvae = NoViableAltException("", 8, 1, self.input)

                    raise nvae

            elif LA8 == 48:
                LA8 = self.input.LA(2)
                if LA8 == 88 or LA8 == 120:
                    alt8 = 1
                elif LA8 == 48 or LA8 == 49 or LA8 == 50 or LA8 == 51 or LA8 == 52 or LA8 == 53 or LA8 == 54 or LA8 == 55:
                    alt8 = 2
                else:
                    alt8 = 3
            elif LA8 == 49 or LA8 == 50 or LA8 == 51 or LA8 == 52 or LA8 == 53 or LA8 == 54 or LA8 == 55 or LA8 == 56 or LA8 == 57:
                alt8 = 3
            else:
                nvae = NoViableAltException("", 8, 0, self.input)

                raise nvae

            if alt8 == 1:
                # proto_lexer.g:126:6: HEX_LITERAL
                pass 
                self.mHEX_LITERAL()


            elif alt8 == 2:
                # proto_lexer.g:127:6: OCTAL_LITERAL
                pass 
                self.mOCTAL_LITERAL()


            elif alt8 == 3:
                # proto_lexer.g:128:6: DECIMAL_LITERAL
                pass 
                self.mDECIMAL_LITERAL()


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INTEGER_LITERAL"



    # $ANTLR start "HEX_DIGIT"
    def mHEX_DIGIT(self, ):

        try:
            # proto_lexer.g:130:20: ( ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' ) )
            # proto_lexer.g:130:22: ( '0' .. '9' | 'a' .. 'f' | 'A' .. 'F' )
            pass 
            if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70) or (97 <= self.input.LA(1) <= 102):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "HEX_DIGIT"



    # $ANTLR start "HEX_LITERAL"
    def mHEX_LITERAL(self, ):

        try:
            # proto_lexer.g:131:22: ( ( '-' )? '0' ( 'x' | 'X' ) ( HEX_DIGIT )+ )
            # proto_lexer.g:131:24: ( '-' )? '0' ( 'x' | 'X' ) ( HEX_DIGIT )+
            pass 
            # proto_lexer.g:131:24: ( '-' )?
            alt9 = 2
            LA9_0 = self.input.LA(1)

            if (LA9_0 == 45) :
                alt9 = 1
            if alt9 == 1:
                # proto_lexer.g:131:24: '-'
                pass 
                self.match(45)



            self.match(48)
            if self.input.LA(1) == 88 or self.input.LA(1) == 120:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # proto_lexer.g:131:43: ( HEX_DIGIT )+
            cnt10 = 0
            while True: #loop10
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if ((48 <= LA10_0 <= 57) or (65 <= LA10_0 <= 70) or (97 <= LA10_0 <= 102)) :
                    alt10 = 1


                if alt10 == 1:
                    # proto_lexer.g:131:43: HEX_DIGIT
                    pass 
                    self.mHEX_DIGIT()


                else:
                    if cnt10 >= 1:
                        break #loop10

                    eee = EarlyExitException(10, self.input)
                    raise eee

                cnt10 += 1




        finally:

            pass

    # $ANTLR end "HEX_LITERAL"



    # $ANTLR start "OCTAL_LITERAL"
    def mOCTAL_LITERAL(self, ):

        try:
            # proto_lexer.g:132:24: ( ( '-' )? '0' ( '0' .. '7' )+ )
            # proto_lexer.g:132:26: ( '-' )? '0' ( '0' .. '7' )+
            pass 
            # proto_lexer.g:132:26: ( '-' )?
            alt11 = 2
            LA11_0 = self.input.LA(1)

            if (LA11_0 == 45) :
                alt11 = 1
            if alt11 == 1:
                # proto_lexer.g:132:26: '-'
                pass 
                self.match(45)



            self.match(48)
            # proto_lexer.g:132:35: ( '0' .. '7' )+
            cnt12 = 0
            while True: #loop12
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if ((48 <= LA12_0 <= 55)) :
                    alt12 = 1


                if alt12 == 1:
                    # proto_lexer.g:132:36: '0' .. '7'
                    pass 
                    self.matchRange(48, 55)


                else:
                    if cnt12 >= 1:
                        break #loop12

                    eee = EarlyExitException(12, self.input)
                    raise eee

                cnt12 += 1




        finally:

            pass

    # $ANTLR end "OCTAL_LITERAL"



    # $ANTLR start "DECIMAL_LITERAL"
    def mDECIMAL_LITERAL(self, ):

        try:
            # proto_lexer.g:133:26: ( ( '0' | ( '-' )? '1' .. '9' ( '0' .. '9' )* ) )
            # proto_lexer.g:133:28: ( '0' | ( '-' )? '1' .. '9' ( '0' .. '9' )* )
            pass 
            # proto_lexer.g:133:28: ( '0' | ( '-' )? '1' .. '9' ( '0' .. '9' )* )
            alt15 = 2
            LA15_0 = self.input.LA(1)

            if (LA15_0 == 48) :
                alt15 = 1
            elif (LA15_0 == 45 or (49 <= LA15_0 <= 57)) :
                alt15 = 2
            else:
                nvae = NoViableAltException("", 15, 0, self.input)

                raise nvae

            if alt15 == 1:
                # proto_lexer.g:133:29: '0'
                pass 
                self.match(48)


            elif alt15 == 2:
                # proto_lexer.g:133:35: ( '-' )? '1' .. '9' ( '0' .. '9' )*
                pass 
                # proto_lexer.g:133:35: ( '-' )?
                alt13 = 2
                LA13_0 = self.input.LA(1)

                if (LA13_0 == 45) :
                    alt13 = 1
                if alt13 == 1:
                    # proto_lexer.g:133:35: '-'
                    pass 
                    self.match(45)



                self.matchRange(49, 57)
                # proto_lexer.g:133:49: ( '0' .. '9' )*
                while True: #loop14
                    alt14 = 2
                    LA14_0 = self.input.LA(1)

                    if ((48 <= LA14_0 <= 57)) :
                        alt14 = 1


                    if alt14 == 1:
                        # proto_lexer.g:133:49: '0' .. '9'
                        pass 
                        self.matchRange(48, 57)


                    else:
                        break #loop14







        finally:

            pass

    # $ANTLR end "DECIMAL_LITERAL"



    # $ANTLR start "STRING_LITERAL"
    def mSTRING_LITERAL(self, ):

        try:
            _type = STRING_LITERAL
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:138:3: ( '\"' STRING_GUTS '\"' )
            # proto_lexer.g:138:6: '\"' STRING_GUTS '\"'
            pass 
            self.match(34)
            self.mSTRING_GUTS()
            self.match(34)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STRING_LITERAL"



    # $ANTLR start "STRING_GUTS"
    def mSTRING_GUTS(self, ):

        try:
            # proto_lexer.g:140:22: ( ( ESCAPE_SEQUENCE | ~ ( '\\\\' | '\"' | '\\n' | '\\r' ) )* )
            # proto_lexer.g:140:24: ( ESCAPE_SEQUENCE | ~ ( '\\\\' | '\"' | '\\n' | '\\r' ) )*
            pass 
            # proto_lexer.g:140:24: ( ESCAPE_SEQUENCE | ~ ( '\\\\' | '\"' | '\\n' | '\\r' ) )*
            while True: #loop16
                alt16 = 3
                LA16_0 = self.input.LA(1)

                if (LA16_0 == 92) :
                    alt16 = 1
                elif ((0 <= LA16_0 <= 9) or (11 <= LA16_0 <= 12) or (14 <= LA16_0 <= 33) or (35 <= LA16_0 <= 91) or (93 <= LA16_0 <= 65535)) :
                    alt16 = 2


                if alt16 == 1:
                    # proto_lexer.g:140:26: ESCAPE_SEQUENCE
                    pass 
                    self.mESCAPE_SEQUENCE()


                elif alt16 == 2:
                    # proto_lexer.g:140:44: ~ ( '\\\\' | '\"' | '\\n' | '\\r' )
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 12) or (14 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 91) or (93 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop16




        finally:

            pass

    # $ANTLR end "STRING_GUTS"



    # $ANTLR start "ESCAPE_SEQUENCE"
    def mESCAPE_SEQUENCE(self, ):

        try:
            # proto_lexer.g:143:3: ( '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' ) | OCTAL_ESCAPE | UNICODE_ESCAPE )
            alt17 = 3
            LA17_0 = self.input.LA(1)

            if (LA17_0 == 92) :
                LA17 = self.input.LA(2)
                if LA17 == 34 or LA17 == 39 or LA17 == 92 or LA17 == 98 or LA17 == 102 or LA17 == 110 or LA17 == 114 or LA17 == 116:
                    alt17 = 1
                elif LA17 == 117:
                    alt17 = 3
                elif LA17 == 48 or LA17 == 49 or LA17 == 50 or LA17 == 51 or LA17 == 52 or LA17 == 53 or LA17 == 54 or LA17 == 55:
                    alt17 = 2
                else:
                    nvae = NoViableAltException("", 17, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 17, 0, self.input)

                raise nvae

            if alt17 == 1:
                # proto_lexer.g:143:6: '\\\\' ( 'b' | 't' | 'n' | 'f' | 'r' | '\\\"' | '\\'' | '\\\\' )
                pass 
                self.match(92)
                if self.input.LA(1) == 34 or self.input.LA(1) == 39 or self.input.LA(1) == 92 or self.input.LA(1) == 98 or self.input.LA(1) == 102 or self.input.LA(1) == 110 or self.input.LA(1) == 114 or self.input.LA(1) == 116:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse



            elif alt17 == 2:
                # proto_lexer.g:144:6: OCTAL_ESCAPE
                pass 
                self.mOCTAL_ESCAPE()


            elif alt17 == 3:
                # proto_lexer.g:145:6: UNICODE_ESCAPE
                pass 
                self.mUNICODE_ESCAPE()



        finally:

            pass

    # $ANTLR end "ESCAPE_SEQUENCE"



    # $ANTLR start "OCTAL_ESCAPE"
    def mOCTAL_ESCAPE(self, ):

        try:
            # proto_lexer.g:149:3: ( '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) ( '0' .. '7' ) | '\\\\' ( '0' .. '7' ) )
            alt18 = 3
            LA18_0 = self.input.LA(1)

            if (LA18_0 == 92) :
                LA18_1 = self.input.LA(2)

                if ((48 <= LA18_1 <= 51)) :
                    LA18_2 = self.input.LA(3)

                    if ((48 <= LA18_2 <= 55)) :
                        LA18_4 = self.input.LA(4)

                        if ((48 <= LA18_4 <= 55)) :
                            alt18 = 1
                        else:
                            alt18 = 2
                    else:
                        alt18 = 3
                elif ((52 <= LA18_1 <= 55)) :
                    LA18_3 = self.input.LA(3)

                    if ((48 <= LA18_3 <= 55)) :
                        alt18 = 2
                    else:
                        alt18 = 3
                else:
                    nvae = NoViableAltException("", 18, 1, self.input)

                    raise nvae

            else:
                nvae = NoViableAltException("", 18, 0, self.input)

                raise nvae

            if alt18 == 1:
                # proto_lexer.g:149:6: '\\\\' ( '0' .. '3' ) ( '0' .. '7' ) ( '0' .. '7' )
                pass 
                self.match(92)
                # proto_lexer.g:149:11: ( '0' .. '3' )
                # proto_lexer.g:149:12: '0' .. '3'
                pass 
                self.matchRange(48, 51)



                # proto_lexer.g:149:22: ( '0' .. '7' )
                # proto_lexer.g:149:23: '0' .. '7'
                pass 
                self.matchRange(48, 55)



                # proto_lexer.g:149:33: ( '0' .. '7' )
                # proto_lexer.g:149:34: '0' .. '7'
                pass 
                self.matchRange(48, 55)





            elif alt18 == 2:
                # proto_lexer.g:150:6: '\\\\' ( '0' .. '7' ) ( '0' .. '7' )
                pass 
                self.match(92)
                # proto_lexer.g:150:11: ( '0' .. '7' )
                # proto_lexer.g:150:12: '0' .. '7'
                pass 
                self.matchRange(48, 55)



                # proto_lexer.g:150:22: ( '0' .. '7' )
                # proto_lexer.g:150:23: '0' .. '7'
                pass 
                self.matchRange(48, 55)





            elif alt18 == 3:
                # proto_lexer.g:151:6: '\\\\' ( '0' .. '7' )
                pass 
                self.match(92)
                # proto_lexer.g:151:11: ( '0' .. '7' )
                # proto_lexer.g:151:12: '0' .. '7'
                pass 
                self.matchRange(48, 55)






        finally:

            pass

    # $ANTLR end "OCTAL_ESCAPE"



    # $ANTLR start "UNICODE_ESCAPE"
    def mUNICODE_ESCAPE(self, ):

        try:
            # proto_lexer.g:155:3: ( '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT )
            # proto_lexer.g:155:6: '\\\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
            pass 
            self.match(92)
            self.match(117)
            self.mHEX_DIGIT()
            self.mHEX_DIGIT()
            self.mHEX_DIGIT()
            self.mHEX_DIGIT()




        finally:

            pass

    # $ANTLR end "UNICODE_ESCAPE"



    # $ANTLR start "BOOL_LITERAL"
    def mBOOL_LITERAL(self, ):

        try:
            _type = BOOL_LITERAL
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:160:14: ( 'true' | 'false' )
            alt19 = 2
            LA19_0 = self.input.LA(1)

            if (LA19_0 == 116) :
                alt19 = 1
            elif (LA19_0 == 102) :
                alt19 = 2
            else:
                nvae = NoViableAltException("", 19, 0, self.input)

                raise nvae

            if alt19 == 1:
                # proto_lexer.g:160:16: 'true'
                pass 
                self.match("true")


            elif alt19 == 2:
                # proto_lexer.g:160:25: 'false'
                pass 
                self.match("false")


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "BOOL_LITERAL"



    # $ANTLR start "FLOAT_LITERAL"
    def mFLOAT_LITERAL(self, ):

        try:
            _type = FLOAT_LITERAL
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:165:3: ( ( '-' )? ( '0' .. '9' )+ '.' ( '0' .. '9' )* ( EXPONENT )? | ( '-' )? '.' ( '0' .. '9' )+ ( EXPONENT )? | ( '-' )? ( '0' .. '9' )+ EXPONENT )
            alt29 = 3
            alt29 = self.dfa29.predict(self.input)
            if alt29 == 1:
                # proto_lexer.g:165:6: ( '-' )? ( '0' .. '9' )+ '.' ( '0' .. '9' )* ( EXPONENT )?
                pass 
                # proto_lexer.g:165:6: ( '-' )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == 45) :
                    alt20 = 1
                if alt20 == 1:
                    # proto_lexer.g:165:6: '-'
                    pass 
                    self.match(45)



                # proto_lexer.g:165:11: ( '0' .. '9' )+
                cnt21 = 0
                while True: #loop21
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if ((48 <= LA21_0 <= 57)) :
                        alt21 = 1


                    if alt21 == 1:
                        # proto_lexer.g:165:12: '0' .. '9'
                        pass 
                        self.matchRange(48, 57)


                    else:
                        if cnt21 >= 1:
                            break #loop21

                        eee = EarlyExitException(21, self.input)
                        raise eee

                    cnt21 += 1
                self.match(46)
                # proto_lexer.g:165:27: ( '0' .. '9' )*
                while True: #loop22
                    alt22 = 2
                    LA22_0 = self.input.LA(1)

                    if ((48 <= LA22_0 <= 57)) :
                        alt22 = 1


                    if alt22 == 1:
                        # proto_lexer.g:165:28: '0' .. '9'
                        pass 
                        self.matchRange(48, 57)


                    else:
                        break #loop22
                # proto_lexer.g:165:39: ( EXPONENT )?
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == 69 or LA23_0 == 101) :
                    alt23 = 1
                if alt23 == 1:
                    # proto_lexer.g:165:39: EXPONENT
                    pass 
                    self.mEXPONENT()





            elif alt29 == 2:
                # proto_lexer.g:166:6: ( '-' )? '.' ( '0' .. '9' )+ ( EXPONENT )?
                pass 
                # proto_lexer.g:166:6: ( '-' )?
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if (LA24_0 == 45) :
                    alt24 = 1
                if alt24 == 1:
                    # proto_lexer.g:166:6: '-'
                    pass 
                    self.match(45)



                self.match(46)
                # proto_lexer.g:166:15: ( '0' .. '9' )+
                cnt25 = 0
                while True: #loop25
                    alt25 = 2
                    LA25_0 = self.input.LA(1)

                    if ((48 <= LA25_0 <= 57)) :
                        alt25 = 1


                    if alt25 == 1:
                        # proto_lexer.g:166:16: '0' .. '9'
                        pass 
                        self.matchRange(48, 57)


                    else:
                        if cnt25 >= 1:
                            break #loop25

                        eee = EarlyExitException(25, self.input)
                        raise eee

                    cnt25 += 1
                # proto_lexer.g:166:27: ( EXPONENT )?
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if (LA26_0 == 69 or LA26_0 == 101) :
                    alt26 = 1
                if alt26 == 1:
                    # proto_lexer.g:166:27: EXPONENT
                    pass 
                    self.mEXPONENT()





            elif alt29 == 3:
                # proto_lexer.g:167:6: ( '-' )? ( '0' .. '9' )+ EXPONENT
                pass 
                # proto_lexer.g:167:6: ( '-' )?
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if (LA27_0 == 45) :
                    alt27 = 1
                if alt27 == 1:
                    # proto_lexer.g:167:6: '-'
                    pass 
                    self.match(45)



                # proto_lexer.g:167:11: ( '0' .. '9' )+
                cnt28 = 0
                while True: #loop28
                    alt28 = 2
                    LA28_0 = self.input.LA(1)

                    if ((48 <= LA28_0 <= 57)) :
                        alt28 = 1


                    if alt28 == 1:
                        # proto_lexer.g:167:12: '0' .. '9'
                        pass 
                        self.matchRange(48, 57)


                    else:
                        if cnt28 >= 1:
                            break #loop28

                        eee = EarlyExitException(28, self.input)
                        raise eee

                    cnt28 += 1
                self.mEXPONENT()


            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FLOAT_LITERAL"



    # $ANTLR start "EXPONENT"
    def mEXPONENT(self, ):

        try:
            # proto_lexer.g:170:19: ( ( 'e' | 'E' ) ( '+' | '-' )? ( '0' .. '9' )+ )
            # proto_lexer.g:170:21: ( 'e' | 'E' ) ( '+' | '-' )? ( '0' .. '9' )+
            pass 
            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # proto_lexer.g:170:31: ( '+' | '-' )?
            alt30 = 2
            LA30_0 = self.input.LA(1)

            if (LA30_0 == 43 or LA30_0 == 45) :
                alt30 = 1
            if alt30 == 1:
                # proto_lexer.g:
                pass 
                if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            # proto_lexer.g:170:42: ( '0' .. '9' )+
            cnt31 = 0
            while True: #loop31
                alt31 = 2
                LA31_0 = self.input.LA(1)

                if ((48 <= LA31_0 <= 57)) :
                    alt31 = 1


                if alt31 == 1:
                    # proto_lexer.g:170:43: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    if cnt31 >= 1:
                        break #loop31

                    eee = EarlyExitException(31, self.input)
                    raise eee

                cnt31 += 1




        finally:

            pass

    # $ANTLR end "EXPONENT"



    # $ANTLR start "IDENTIFIER"
    def mIDENTIFIER(self, ):

        try:
            _type = IDENTIFIER
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:173:12: ( ( '_' )* ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' )* )
            # proto_lexer.g:173:14: ( '_' )* ( 'a' .. 'z' | 'A' .. 'Z' ) ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' )*
            pass 
            # proto_lexer.g:173:14: ( '_' )*
            while True: #loop32
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (LA32_0 == 95) :
                    alt32 = 1


                if alt32 == 1:
                    # proto_lexer.g:173:14: '_'
                    pass 
                    self.match(95)


                else:
                    break #loop32
            if (65 <= self.input.LA(1) <= 90) or (97 <= self.input.LA(1) <= 122):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # proto_lexer.g:173:42: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' )*
            while True: #loop33
                alt33 = 2
                LA33_0 = self.input.LA(1)

                if ((48 <= LA33_0 <= 57) or (65 <= LA33_0 <= 90) or LA33_0 == 95 or (97 <= LA33_0 <= 122)) :
                    alt33 = 1


                if alt33 == 1:
                    # proto_lexer.g:
                    pass 
                    if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop33



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "IDENTIFIER"



    # $ANTLR start "QUALIFIED_IDENTIFIER"
    def mQUALIFIED_IDENTIFIER(self, ):

        try:
            _type = QUALIFIED_IDENTIFIER
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:174:22: ( IDENTIFIER ( '.' IDENTIFIER )+ )
            # proto_lexer.g:174:24: IDENTIFIER ( '.' IDENTIFIER )+
            pass 
            self.mIDENTIFIER()
            # proto_lexer.g:174:35: ( '.' IDENTIFIER )+
            cnt34 = 0
            while True: #loop34
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == 46) :
                    alt34 = 1


                if alt34 == 1:
                    # proto_lexer.g:174:36: '.' IDENTIFIER
                    pass 
                    self.match(46)
                    self.mIDENTIFIER()


                else:
                    if cnt34 >= 1:
                        break #loop34

                    eee = EarlyExitException(34, self.input)
                    raise eee

                cnt34 += 1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "QUALIFIED_IDENTIFIER"



    # $ANTLR start "FIELD_IDENTIFIER"
    def mFIELD_IDENTIFIER(self, ):

        try:
            _type = FIELD_IDENTIFIER
            _channel = DEFAULT_CHANNEL

            # proto_lexer.g:175:18: ( '.' IDENTIFIER )
            # proto_lexer.g:175:20: '.' IDENTIFIER
            pass 
            self.match(46)
            self.mIDENTIFIER()



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FIELD_IDENTIFIER"



    def mTokens(self):
        # proto_lexer.g:1:8: ( COMMENT | WHITESPACE | PACKAGE_LITERAL | IMPORT_LITERAL | OPTION_LITERAL | ENUM_LITERAL | MESSAGE_LITERAL | EXTEND_LITERAL | EXTENSIONS_DEF_LITERAL | EXTENSIONS_TO_LITERAL | EXTENSIONS_MAX_LITERAL | SERVICE_LITERAL | RETURNS_LITERAL | RPC_LITERAL | BLOCK_OPEN | BLOCK_CLOSE | PAREN_OPEN | PAREN_CLOSE | BRACKET_OPEN | BRACKET_CLOSE | EQUALS | COLON | COMMA | ITEM_TERMINATOR | PROTOBUF_SCOPE_LITERAL | PROTOBUF_TYPE_LITERAL | INTEGER_LITERAL | STRING_LITERAL | BOOL_LITERAL | FLOAT_LITERAL | IDENTIFIER | QUALIFIED_IDENTIFIER | FIELD_IDENTIFIER )
        alt35 = 33
        alt35 = self.dfa35.predict(self.input)
        if alt35 == 1:
            # proto_lexer.g:1:10: COMMENT
            pass 
            self.mCOMMENT()


        elif alt35 == 2:
            # proto_lexer.g:1:18: WHITESPACE
            pass 
            self.mWHITESPACE()


        elif alt35 == 3:
            # proto_lexer.g:1:29: PACKAGE_LITERAL
            pass 
            self.mPACKAGE_LITERAL()


        elif alt35 == 4:
            # proto_lexer.g:1:45: IMPORT_LITERAL
            pass 
            self.mIMPORT_LITERAL()


        elif alt35 == 5:
            # proto_lexer.g:1:60: OPTION_LITERAL
            pass 
            self.mOPTION_LITERAL()


        elif alt35 == 6:
            # proto_lexer.g:1:75: ENUM_LITERAL
            pass 
            self.mENUM_LITERAL()


        elif alt35 == 7:
            # proto_lexer.g:1:88: MESSAGE_LITERAL
            pass 
            self.mMESSAGE_LITERAL()


        elif alt35 == 8:
            # proto_lexer.g:1:104: EXTEND_LITERAL
            pass 
            self.mEXTEND_LITERAL()


        elif alt35 == 9:
            # proto_lexer.g:1:119: EXTENSIONS_DEF_LITERAL
            pass 
            self.mEXTENSIONS_DEF_LITERAL()


        elif alt35 == 10:
            # proto_lexer.g:1:142: EXTENSIONS_TO_LITERAL
            pass 
            self.mEXTENSIONS_TO_LITERAL()


        elif alt35 == 11:
            # proto_lexer.g:1:164: EXTENSIONS_MAX_LITERAL
            pass 
            self.mEXTENSIONS_MAX_LITERAL()


        elif alt35 == 12:
            # proto_lexer.g:1:187: SERVICE_LITERAL
            pass 
            self.mSERVICE_LITERAL()


        elif alt35 == 13:
            # proto_lexer.g:1:203: RETURNS_LITERAL
            pass 
            self.mRETURNS_LITERAL()


        elif alt35 == 14:
            # proto_lexer.g:1:219: RPC_LITERAL
            pass 
            self.mRPC_LITERAL()


        elif alt35 == 15:
            # proto_lexer.g:1:231: BLOCK_OPEN
            pass 
            self.mBLOCK_OPEN()


        elif alt35 == 16:
            # proto_lexer.g:1:242: BLOCK_CLOSE
            pass 
            self.mBLOCK_CLOSE()


        elif alt35 == 17:
            # proto_lexer.g:1:254: PAREN_OPEN
            pass 
            self.mPAREN_OPEN()


        elif alt35 == 18:
            # proto_lexer.g:1:265: PAREN_CLOSE
            pass 
            self.mPAREN_CLOSE()


        elif alt35 == 19:
            # proto_lexer.g:1:277: BRACKET_OPEN
            pass 
            self.mBRACKET_OPEN()


        elif alt35 == 20:
            # proto_lexer.g:1:290: BRACKET_CLOSE
            pass 
            self.mBRACKET_CLOSE()


        elif alt35 == 21:
            # proto_lexer.g:1:304: EQUALS
            pass 
            self.mEQUALS()


        elif alt35 == 22:
            # proto_lexer.g:1:311: COLON
            pass 
            self.mCOLON()


        elif alt35 == 23:
            # proto_lexer.g:1:317: COMMA
            pass 
            self.mCOMMA()


        elif alt35 == 24:
            # proto_lexer.g:1:323: ITEM_TERMINATOR
            pass 
            self.mITEM_TERMINATOR()


        elif alt35 == 25:
            # proto_lexer.g:1:339: PROTOBUF_SCOPE_LITERAL
            pass 
            self.mPROTOBUF_SCOPE_LITERAL()


        elif alt35 == 26:
            # proto_lexer.g:1:362: PROTOBUF_TYPE_LITERAL
            pass 
            self.mPROTOBUF_TYPE_LITERAL()


        elif alt35 == 27:
            # proto_lexer.g:1:384: INTEGER_LITERAL
            pass 
            self.mINTEGER_LITERAL()


        elif alt35 == 28:
            # proto_lexer.g:1:400: STRING_LITERAL
            pass 
            self.mSTRING_LITERAL()


        elif alt35 == 29:
            # proto_lexer.g:1:415: BOOL_LITERAL
            pass 
            self.mBOOL_LITERAL()


        elif alt35 == 30:
            # proto_lexer.g:1:428: FLOAT_LITERAL
            pass 
            self.mFLOAT_LITERAL()


        elif alt35 == 31:
            # proto_lexer.g:1:442: IDENTIFIER
            pass 
            self.mIDENTIFIER()


        elif alt35 == 32:
            # proto_lexer.g:1:453: QUALIFIED_IDENTIFIER
            pass 
            self.mQUALIFIED_IDENTIFIER()


        elif alt35 == 33:
            # proto_lexer.g:1:474: FIELD_IDENTIFIER
            pass 
            self.mFIELD_IDENTIFIER()







    # lookup tables for DFA #7

    DFA7_eot = DFA.unpack(
        u"\46\uffff"
        )

    DFA7_eof = DFA.unpack(
        u"\46\uffff"
        )

    DFA7_min = DFA.unpack(
        u"\1\142\1\uffff\1\151\1\156\1\151\1\146\1\157\1\uffff\1\170\1\164"
        u"\2\156\1\151\3\uffff\1\145\1\63\2\164\1\170\1\144\2\uffff\2\63"
        u"\1\145\1\63\4\uffff\1\144\2\uffff\1\63\2\uffff"
        )

    DFA7_max = DFA.unpack(
        u"\1\165\1\uffff\1\154\1\156\1\151\1\164\1\171\1\uffff\1\170\1\164"
        u"\2\156\1\151\3\uffff\1\145\1\66\2\164\1\170\1\144\2\uffff\2\66"
        u"\1\145\1\66\4\uffff\1\144\2\uffff\1\66\2\uffff"
        )

    DFA7_accept = DFA.unpack(
        u"\1\uffff\1\1\5\uffff\1\2\5\uffff\1\16\1\15\1\17\6\uffff\1\3\1\4"
        u"\4\uffff\1\5\1\6\1\7\1\10\1\uffff\1\11\1\12\1\uffff\1\13\1\14"
        )

    DFA7_special = DFA.unpack(
        u"\46\uffff"
        )

            
    DFA7_transition = [
        DFA.unpack(u"\1\6\1\uffff\1\1\1\uffff\1\2\2\uffff\1\3\11\uffff\1"
        u"\5\1\uffff\1\4"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\10\2\uffff\1\7"),
        DFA.unpack(u"\1\11"),
        DFA.unpack(u"\1\12"),
        DFA.unpack(u"\1\14\2\uffff\1\13\12\uffff\1\15"),
        DFA.unpack(u"\1\16\11\uffff\1\17"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\20"),
        DFA.unpack(u"\1\21"),
        DFA.unpack(u"\1\22"),
        DFA.unpack(u"\1\23"),
        DFA.unpack(u"\1\24"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\25"),
        DFA.unpack(u"\1\26\2\uffff\1\27"),
        DFA.unpack(u"\1\30"),
        DFA.unpack(u"\1\31"),
        DFA.unpack(u"\1\32"),
        DFA.unpack(u"\1\33"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\34\2\uffff\1\35"),
        DFA.unpack(u"\1\36\2\uffff\1\37"),
        DFA.unpack(u"\1\40"),
        DFA.unpack(u"\1\41\2\uffff\1\42"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\44\2\uffff\1\45"),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #7

    class DFA7(DFA):
        pass


    # lookup tables for DFA #29

    DFA29_eot = DFA.unpack(
        u"\6\uffff"
        )

    DFA29_eof = DFA.unpack(
        u"\6\uffff"
        )

    DFA29_min = DFA.unpack(
        u"\1\55\2\56\3\uffff"
        )

    DFA29_max = DFA.unpack(
        u"\2\71\1\145\3\uffff"
        )

    DFA29_accept = DFA.unpack(
        u"\3\uffff\1\2\1\3\1\1"
        )

    DFA29_special = DFA.unpack(
        u"\6\uffff"
        )

            
    DFA29_transition = [
        DFA.unpack(u"\1\1\1\3\1\uffff\12\2"),
        DFA.unpack(u"\1\3\1\uffff\12\2"),
        DFA.unpack(u"\1\5\1\uffff\12\2\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #29

    class DFA29(DFA):
        pass


    # lookup tables for DFA #35

    DFA35_eot = DFA.unpack(
        u"\3\uffff\10\42\12\uffff\4\42\1\uffff\2\74\3\uffff\3\42\2\uffff"
        u"\7\42\1\110\16\42\3\uffff\2\74\1\uffff\7\42\1\141\1\uffff\10\42"
        u"\1\152\14\42\1\167\2\42\1\uffff\1\172\7\42\1\uffff\5\42\1\u0089"
        u"\3\42\2\u0089\1\42\1\uffff\2\42\1\uffff\11\42\1\u0089\1\42\1\172"
        u"\2\42\1\uffff\1\u0089\1\42\1\u009f\1\u00a1\1\u00a2\3\42\2\u0089"
        u"\1\42\1\u0089\3\42\1\u0089\2\42\2\u0089\1\u00ad\1\uffff\1\42\2"
        u"\uffff\1\42\1\u00b0\1\u00b1\2\42\1\u00b4\2\42\2\u0089\1\uffff\1"
        u"\u00b7\1\42\2\uffff\2\u0089\1\uffff\2\u00b7\1\uffff\1\42\1\u00ba"
        u"\1\uffff"
        )

    DFA35_eof = DFA.unpack(
        u"\u00bb\uffff"
        )

    DFA35_min = DFA.unpack(
        u"\1\11\2\uffff\10\56\12\uffff\7\56\1\uffff\1\60\1\101\3\56\2\uffff"
        u"\27\56\2\uffff\2\56\1\uffff\10\56\1\uffff\30\56\1\uffff\10\56\1"
        u"\uffff\14\56\1\uffff\2\56\1\uffff\16\56\1\uffff\25\56\1\uffff\1"
        u"\56\2\uffff\12\56\1\uffff\2\56\2\uffff\2\56\1\uffff\2\56\1\uffff"
        u"\2\56\1\uffff"
        )

    DFA35_max = DFA.unpack(
        u"\1\175\2\uffff\10\172\12\uffff\4\172\1\71\2\145\1\uffff\5\172\2"
        u"\uffff\26\172\1\170\2\uffff\2\145\1\uffff\10\172\1\uffff\30\172"
        u"\1\uffff\10\172\1\uffff\14\172\1\uffff\2\172\1\uffff\16\172\1\uffff"
        u"\25\172\1\uffff\1\172\2\uffff\12\172\1\uffff\2\172\2\uffff\2\172"
        u"\1\uffff\2\172\1\uffff\2\172\1\uffff"
        )

    DFA35_accept = DFA.unpack(
        u"\1\uffff\1\1\1\2\10\uffff\1\17\1\20\1\21\1\22\1\23\1\24\1\25\1"
        u"\26\1\27\1\30\7\uffff\1\34\5\uffff\1\37\1\40\27\uffff\1\36\1\33"
        u"\2\uffff\1\41\10\uffff\1\12\30\uffff\1\13\10\uffff\1\16\14\uffff"
        u"\1\6\2\uffff\1\35\16\uffff\1\32\25\uffff\1\4\1\uffff\1\5\1\10\12"
        u"\uffff\1\3\2\uffff\1\7\1\14\2\uffff\1\15\2\uffff\1\31\2\uffff\1"
        u"\11"
        )

    DFA35_special = DFA.unpack(
        u"\u00bb\uffff"
        )

            
    DFA35_transition = [
        DFA.unpack(u"\2\2\1\uffff\2\2\22\uffff\1\2\1\uffff\1\34\5\uffff\1"
        u"\15\1\16\2\uffff\1\23\1\31\1\35\1\1\1\32\11\33\1\22\1\24\1\uffff"
        u"\1\21\3\uffff\32\37\1\17\1\uffff\1\20\1\uffff\1\36\1\uffff\1\37"
        u"\1\30\1\37\1\25\1\6\1\26\2\37\1\4\3\37\1\7\1\37\1\5\1\3\1\37\1"
        u"\12\1\11\1\10\1\27\5\37\1\13\1\uffff\1\14"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\1\40\31\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\14\41\1\44\1\45\14\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\17\41\1\46\12\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\15\41\1\47\11\41\1\50\2\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\1\52\3\41\1\51\25\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\16\41\1\53\2\41\1\54\10\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\4\41\1\55\1\57\2\41\1\56\12\41\1\60\6\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\4\41\1\61\12\41\1\62\12\41"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\16\41\1\63\13\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\1\66\7\41\1\65\2\41\1\64\16\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\10\41\1\67\21\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\16\41\1\70\11\41\1\71\1\41"),
        DFA.unpack(u"\1\73\1\uffff\1\72\11\33"),
        DFA.unpack(u"\1\73\1\uffff\10\75\2\73\13\uffff\1\73\37\uffff\1\73"),
        DFA.unpack(u"\1\73\1\uffff\12\76\13\uffff\1\73\37\uffff\1\73"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\73\7\uffff\32\77\4\uffff\1\77\1\uffff\32\77"),
        DFA.unpack(u"\32\37\4\uffff\1\36\1\uffff\32\37"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\2\41\1\100\27\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\17\41\1\101\12\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\23\41\1\102\6\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\23\41\1\103\6\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\24\41\1\104\5\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\23\41\1\105\6\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\22\41\1\106\7\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\27\41\1\107\2\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\24\41\1\111\5\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\21\41\1\112\10\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\15\41\1\113\14\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\10\41\1\114\21\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\21\41\1\115\10\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\17\41\1\120\1\117\2\41\1\116\6\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\2\41\1\121\27\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\24\41\1\122\5\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\16\41\1\123\13\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\27\41\1\124\2\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\13\41\1\125\16\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\15\41\1\126\14\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\16\41\1\127\13\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\23\41\1\130\6\41"),
        DFA.unpack(u"\1\73\1\uffff\10\75\2\73\13\uffff\1\73\22\uffff\1\74"
        u"\14\uffff\1\73\22\uffff\1\74"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\73\1\uffff\10\75\2\73\13\uffff\1\73\37\uffff\1\73"),
        DFA.unpack(u"\1\73\1\uffff\12\76\13\uffff\1\73\37\uffff\1\73"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\12\41\1\131\17\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\16\41\1\132\13\41"),
        DFA.unpack(u"\1\43\1\uffff\3\41\1\133\2\41\1\134\3\41\7\uffff\32"
        u"\41\4\uffff\1\41\1\uffff\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\10\41\1\135\21\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\14\41\1\136\15\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\4\41\1\137\25\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\22\41\1\140\7\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\4\41\1\142\25\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\25\41\1\143\4\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\23\41\1\144\6\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\27\41\1\145\2\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\10\41\1\146\21\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\24\41\1\147\5\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\24\41\1\150\5\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\4\41\1\151\25\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\1\41\1\153\30\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\1\154\31\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\4\41\1\155\25\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\22\41\1\156\7\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\23\41\1\157\6\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\13\41\1\160\16\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\4\41\1\161\25\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\1\162\31\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\21\41\1\163\10\41"),
        DFA.unpack(u"\1\43\1\uffff\2\41\1\164\7\41\7\uffff\32\41\4\uffff"
        u"\1\41\1\uffff\32\41"),
        DFA.unpack(u"\1\43\1\uffff\4\41\1\165\5\41\7\uffff\32\41\4\uffff"
        u"\1\41\1\uffff\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\16\41\1\166\13\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\15\41\1\170\14\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\1\171\31\41"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\10\41\1\173\21\41"),
        DFA.unpack(u"\1\43\1\uffff\3\41\1\174\2\41\1\175\3\41\7\uffff\32"
        u"\41\4\uffff\1\41\1\uffff\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\4\41\1\176\25\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\15\41\1\177\14\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\21\41\1\u0080\10\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\10\41\1\u0081\21\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\1\u0082\31\41"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\13\41\1\u0083\16\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\23\41\1\u0084\6\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\3\41\1\u0085\26\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\4\41\1\u0086\25\41"),
        DFA.unpack(u"\1\43\1\uffff\3\41\1\u0087\2\41\1\u0088\3\41\7\uffff"
        u"\32\41\4\uffff\1\41\1\uffff\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\22\41\1\u008a\7\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\6\41\1\u008b\23\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\23\41\1\u008c\6\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\15\41\1\u008d\14\41"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\3\41\1\u008e\16\41\1\u008f\7\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\6\41\1\u0090\23\41"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\2\41\1\u0091\27\41"),
        DFA.unpack(u"\1\43\1\uffff\2\41\1\u0092\7\41\7\uffff\32\41\4\uffff"
        u"\1\41\1\uffff\32\41"),
        DFA.unpack(u"\1\43\1\uffff\4\41\1\u0093\5\41\7\uffff\32\41\4\uffff"
        u"\1\41\1\uffff\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\3\41\1\u0094\26\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\6\41\1\u0095\23\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\15\41\1\u0096\14\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\21\41\1\u0097\10\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\23\41\1\u0098\6\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\4\41\1\u0099\25\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\3\41\1\u009a\2\41\1\u009b\3\41\7\uffff"
        u"\32\41\4\uffff\1\41\1\uffff\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\2\41\1\u009c\7\41\7\uffff\32\41\4\uffff"
        u"\1\41\1\uffff\32\41"),
        DFA.unpack(u"\1\43\1\uffff\4\41\1\u009d\5\41\7\uffff\32\41\4\uffff"
        u"\1\41\1\uffff\32\41"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\4\41\1\u009e\25\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\1\u00a0\31\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\10\41\1\u00a3\21\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\4\41\1\u00a4\25\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\4\41\1\u00a5\25\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\3\41\1\u00a6\2\41\1\u00a7\3\41\7\uffff"
        u"\32\41\4\uffff\1\41\1\uffff\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\22\41\1\u00a8\7\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\4\41\1\u00a9\25\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\4\41\1\u00aa\25\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\2\41\1\u00ab\7\41\7\uffff\32\41\4\uffff"
        u"\1\41\1\uffff\32\41"),
        DFA.unpack(u"\1\43\1\uffff\4\41\1\u00ac\5\41\7\uffff\32\41\4\uffff"
        u"\1\41\1\uffff\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\13\41\1\u00ae\16\41"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\16\41\1\u00af\13\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\2\41\1\u00b2\7\41\7\uffff\32\41\4\uffff"
        u"\1\41\1\uffff\32\41"),
        DFA.unpack(u"\1\43\1\uffff\4\41\1\u00b3\5\41\7\uffff\32\41\4\uffff"
        u"\1\41\1\uffff\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\3\41\1\u00b5\26\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\3\41\1\u00b6\26\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\15\41\1\u00b8\14\41"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\22\41\1\u00b9\7\41"),
        DFA.unpack(u"\1\43\1\uffff\12\41\7\uffff\32\41\4\uffff\1\41\1\uffff"
        u"\32\41"),
        DFA.unpack(u"")
    ]

    # class definition for DFA #35

    class DFA35(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(proto_lexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
